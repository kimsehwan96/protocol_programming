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
        self.body = {}
        self.tailor = {}
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

    def data_length(self):
        pass
    #명령어의 특정 부분 파싱해서 길이 확인 -> vaildation check에 활용 될 예정임.

    def validation(self):
        if self.oper in command.operands:
            return True
        else:
            return True
        #TODO: 명령어가 명령어 목록에 있는지 체크, 이후에 factoryCode 및 chimneyCode 체크 해서 True 혹은 False 반환.
        #현재는 test용으로 무조건 True 반환 ++ check crc까지 통과하면.
        # -> vaildation 체크의 진입점은 get_operands // 파싱한 명령어가 명령어 목록에 있는지 체크함.

    def get_operands(self):
        tmp_buffer = self.get_data_recv()
        operands = tmp_buffer[0:4] #명령어는 항상 고정길이.
        self.oper = operands.decode(encoding = encoding)
        return self.oper #str 'TDAT' return

    def check_crc(self, data):
        pass

    def message(self):
        msg = "테스트용 메시지 입니다."
        return msg #string 형태로 return?

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
    
    @staticmethod
    def send(self):
        print("message sended")

""" 위 클래스는 -> 새로운 클래스로 만들어서, 팩토리에서 쓰일 것에 기본 틀로 상속해야 할듯. 여기있으면 안됨 """



if __name__ == "__main__":
    data_gather = DataGather(ip_addr, port_number)
    data_gather.get_operands()
    #Command.factory('TDAT').do()
    DataGather.factory('TDAT').do()