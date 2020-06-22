import abc
import time
import socket
import datetime
import json
import traceback

filepath = 'profile.json'
encoding = 'ascii'

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
        self.client = None
        if self.client == None:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip_addr, port_number))
            self.client = client
        self.buffer = None

    def check_init_frame(self):
        pass

    def devide_header(self):
        pass

    def get_operands(self):
        operands = self.client.recv(4)
        oper = operands.decode(encoding = encoding)
        return oper #str 'TDAT' return



if __name__ == "__main__":
    data_gather = DataGather(ip_addr, port_number)
    data_gather.get_operands()