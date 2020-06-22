# -*- coding: utf-8 -*- 

import socket
import struct
import argparse
from time import sleep


operands = [
    "TDAT",
    "PDUM",
    "TDUM",
    "TFDT",
    "PSEP",
    "TVER",
    "PTIM",
    "PUPG",
    "TUPG",
    "PVER",
    "DVER",
    "PSET"

]


def run_server(port=9999):
    #TDAT 명령 전송
    #data = convert_operands(operands[0])
    text_msg = 'TDAT1200001001  582002251300'
    msg = []
    for i in text_msg:
        msg.append(ord(i))  
    data = struct.pack('=28b', *msg)
    conn.sendall(data)
    print("send message {}".format(data))

def convert_operands(data):
    tmp_list = [ ord(i) for i in data ]
    send_data = struct.pack('=4i', *tmp_list)
    return send_data

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    while True:
        run_server()
        sleep(1)