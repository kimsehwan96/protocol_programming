import abc
import time
import socket
import datetime
import json
import traceback
import command

filepath = 'profile.json'
encoding = 'ascii'
operands = command.operands #dict

with open(filepath, 'r') as f:
    try:
        response = json.load(f)
    except Exception as e:
        print(traceback.format_exc())

ip_addr = response['target_ip']
port_number = int(response['target_port'])

class DataGather(object):
    
    def __init__(self, ip, port):
        self.ip = ip_addr
        self.port = port_number
        self.buffer = None
        self.client = None
        if self.client == None:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip_addr, port_number))
            self.client = client
        else:
            pass
        self.oper

    def get_data_recv(self):
        self.buffer = self.client.recv(1024)
        return self.buffer

    def check_init_frame(self):
        if self.get_operands in operands:
            return True
        else:
            return False

    def devide_header(self):
        if self.oper == None:
            pass
        else:
            pass

    def get_operands(self):
        tmp_buffer = self.get_data_recv()
        operands = tmp_buffer[0:4]
        self.oper = operands.decode(encoding = encoding)
        return self.oper #str 'TDAT' return



if __name__ == "__main__":
    data_gather = DataGather(ip_addr, port_number)
    data_gather.get_operands()