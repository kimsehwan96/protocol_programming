import abc
import time
import socket
import datetime
import json
import traceback
import command
from command import Command

filepath = 'profile.json'
encoding = 'ascii'

with open(filepath, 'r') as f:
    try:
        response = json.load(f)
    except Exception as e:
        print(traceback.format_exc())

ip_addr = response['target_ip']
port_number = int(response['target_port'])

class DataFramer(Command):
    
    def __init__(self, ip, port):
        self.ip = ip_addr
        self.port = port_number
        self.buffer = None
        self.client = None
        self.header = {
            'operand' : None,
            'factoryCode' : None,
            'chimneyCode' : None,
            'length' : None,
            'startedAt' : None,
        }
        if self.client == None:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip_addr, port_number))
            self.client = client
        else:
            pass
        self.oper = None

    def validation(self):
        pass

    def send(self):
        pass

class DataGather(DataFramer):

    """ 
    this class will detecting header & do some needed logic

    """

    def devide_header(self):
        if self.oper == None:
            pass
        else:
            pass

    def get_data_recv(self):
        self.buffer = self.client.recv(1024)
        return self.buffer

    def check_init_frame(self):
        if self.oper in command.operands:
            return True
        else:
            return False
    def get_operands(self):
        tmp_buffer = self.get_data_recv()
        operands = tmp_buffer[0:4]
        self.oper = operands.decode(encoding = encoding)
        return self.oper #str 'TDAT' return

    def check_crc(self, data):
        pass

class DataSender(DataFramer):
    """
    this class will make some header & body & tail for server
    """
    def making_header(self):
        pass

    def making_body(self):
        pass

    def making_tail(self):
        pass

    def send(self):
        pass




if __name__ == "__main__":
    data_gather = DataGather(ip_addr, port_number)
    data_gather.get_operands()
    #Command.factory('TDAT').do()
    DataGather.factory('TDAT').do()