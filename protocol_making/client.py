from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 9999))

print('연결 확인 됐습니다.')
clientSock.send('I am a client'.encode('utf-8'))

print('메시지를 전송했습니다.')

while True:
    data = clientSock.recv(1024)
   # print('받은 데이터 : ', data.decode('utf-8'))
    print("raw data :", data) # byte datas.

    asciis = []

    for idx in data:
       asciis.append(hex(idx))

    #print(asciis)
    data_2 = clientSock.recv(4)
    print("this is first 4 bytes : {}".format(data_2
    ))
    if data_2 == b'TDAT':
        data_2 += clientSock.recv(5)
        print("another data",data_2)