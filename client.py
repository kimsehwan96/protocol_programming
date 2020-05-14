import os
import sys
import socket
import struct

import util
from util import Message

from msgheader import Header
from msgbody import BodyData
from msgbody import BodyRequest
from msgbody import BodyResponse
from msgbody import BodyResult

from message_util import MessageUtil

CHUNK_SIZE = 4096

if   __name__ == '__main__':
    if len(sys.argv) < 4:
        print("사용법 : {0} <Server IP> <File Path> <file Name>".
              format(sys.argv[0]))
        sys.exit(0)

    serverIp   = sys.argv[1]
    serverPort = 5425
    filepath   = sys.argv[2]
    filename = sys.argv[3]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 소켓을 생성한다.
        
    try:
        print("서버:{0}/{1}".format(serverIp, serverPort))        
    
        sock.connect((serverIp, serverPort)) # 접속 요청을 수락한다.

        msgId = 0



        reqMsg = Message()        
        filesize = os.path.getsize(filepath)
        print(filesize)
        reqMsg.Body = BodyRequest(None)
        reqMsg.Body.FILESIZE = filesize
        reqMsg.Body.FILENAME = sys.argv[3]
       
    
        msgId += 1
        reqMsg.Header = Header(None)
        reqMsg.Header.MSGID = msgId
        reqMsg.Header.MSGTYPE = util.REQ_FILE_SEND
        reqMsg.Header.BODYLEN = reqMsg.Body.GetSize()
        reqMsg.Header.FRAGMENTED = util.NOT_FRAGMENTED
        reqMsg.Header.LASTMSG = util.LASTMSG
        reqMsg.Header.SEQ = 0
          
        MessageUtil.send(sock, reqMsg) # 클라이언트는 서버에 접속하자마자 파일 전송 요청 메세지를 보낸다.
        rspMsg = MessageUtil.receive(sock) # 그리고 서버의 응답을 받는다.

        if rspMsg.Header.MSGTYPE != util.REP_FILE_SEND:
            print("정상적인 서버 응답이 아닙니다.{0}".
                format(rspMsg.Header.MSGTYPE))
            exit(0)

        if rspMsg.Body.RESPONSE == util.DENIED:
            print("서버에서 파일 전송을 거부했습니다.")
            exit(0)

        with open(filepath, 'rb') as file: # 서버에서 전송 요청을 수락했다면, 파일을 열어 서버로 보낼 준비를 한다.
            totalRead = 0
            msgSeq = 0 #ushort
            fragmented = 0 #byte
            if filesize < CHUNK_SIZE:
                fragmented = util.NOT_FRAGMENTED
            else:
                fragmented = util.FRAGMENTED
    
            while totalRead < filesize:
                rbytes = file.read(CHUNK_SIZE)
                totalRead += len(rbytes)

                fileMsg = Message()            
                fileMsg.Body = BodyData(rbytes) # 모든 파일의 내용이 전송될 때까지 파일을 0x03 메세지에 담아 서버로 보낸다.

                header = Header(None)
                header.MSGID = msgId
                header.MSGTYPE = util.FILE_SEND_DATA
                header.BODYLEN = fileMsg.Body.GetSize()
                header.FRAGMENTED = fragmented
                if totalRead < filesize:
                    header.LASTMSG = util.NOT_LASTMSG
                else:
                    header.LASTMSG = util.LASTMSG

                header.SEQ = msgSeq
                msgSeq += 1
            
                fileMsg.Header = header
                print("#", end = '')

                MessageUtil.send(sock, fileMsg)

            print()

            rstMsg = MessageUtil.receive(sock) # 서버에서 파일을 제대로 받았는지에 대한 응답을 받는다.
                    
            result = rstMsg.Body
            print("파일 전송 성공 : {0}".
                format(result.RESULT == util.SUCCESS))

    except Exception as err:
        print("예외가 발생했습니다.")
        print(err)

    sock.close()    
    print("클라이언트를 종료합니다.")