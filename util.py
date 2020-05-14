# magic numbers

REQ_FILE_SEND = 0x01 #메시지 타입 상수 정의
REP_FILE_SEND = 0x02
FILE_SEND_DATA = 0x03
FILE_SEND_RES = 0x04

NOT_FRAGMENTED = 0x00 # 파일 분할 여부 상수 정의
FRAGMENTED = -0x01 

NOT_LASTMSG = 0x00 # 분할된 메시지의 마지막 여부 
LASTMSG = 0x01

ACCEPTED = 0x00 # 파일 전솓 수락 여부 
DENIED = 0x01

FAIL = 0x00
SUCCESS = 0x01



class ISerializable:
    """ 메시지 헤더 바디는 모두 이 클래스를 상속한다
    """
    def GetBytes(self):
        pass

    def GetSize(self):
        pass

class Message(ISerializable): #상속됨
    def __init__(self):
        #초기 파라미터 설정
        self.Header = ISerializable()
        self.Body = ISerializable()

    def GetBytes(self):
        buffer = bytes(self.GetSize())

        header = self.Header.GetBytes()
        body = self.Body.GetBytes()

        return header + body