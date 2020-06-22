# -*- coding: utf-8 -*- 

from socket import *
from time import sleep
from message_format import Header

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 9999))

print('연결 확인 됐습니다.')

while True:
    data = clientSock.recv(1024)
    h = Header(data)
    print('받은 데이터 : ', data.decode('utf-8'))
    print(h.GetBytes())
    print(h.GetSize())
    print(h.GetHex())
    sleep(1)