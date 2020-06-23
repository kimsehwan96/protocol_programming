import abc
import time
import socket
import datetime
import json
import traceback
import struct

from util import computeCRC
from util import checkCRC
#tailor의 crc vaildation check를 위해 필요함.

#데이터 처리는 hex ascii로. byte로 받은 데이터를 ascii -> hex로 변환.
dt = datetime.datetime.now()
DATETIME =str(dt.year) + str(dt.month) + str(dt.day) + str(dt.hour) + str(dt.minute)
ACK = 0x06
NAK = 0x15
EOT = 0x04
filepath = 'profile.json'
encoding = 'ascii'
operands = {
    "TDAT",
    "PDUM",
    "TDUM",
    "TFDT",
    "PSEP",
    "TVER",
    "PTIM",
    "PUPG",
    "TUPG",
    "TCNG",
    "PVER",
    "DVER",
    "PSET"
}

with open(filepath, 'r') as f:
    try:
        response = json.load(f)
    except Exception as e:
        print(traceback.format_exc())

ip_addr = response['target_ip']
port_number = int(response['target_port'])
factoryCode = response['factoryCode']
chimeyCode = response['chimeyCode']


class Command:

    __metaclass__ = abc.ABCMeta

    def do(self):
        if self.validation():
            self.send()
        else:
            raise Exception

    @abc.abstractmethod    
    def send(self):
        pass

    @abc.abstractmethod
    def validation(self):
        pass
    #vaildation will return True or False

    @staticmethod
    def factory(command: str):
        return eval(command+"()")

    #수신된 각 명령어 마다 해당 class 호출 될 수 있게.

"""
below objects are describing what process sholud be done in specific command.
아래 코드들은 명령어 (header + body + tailor 가 모두 수집되고, vaildation 체크가 끝났을 때 돌아야 하는 로직 임.)
즉 DataGather 클래스에서 모든 checking logic 통과 / header + body + tailor 나눈 뒤에, 해당 헤더 바디 테일을 보고 로직이 돌아야 함

"""

class ReceiveCmd(Command):
    def send(self):
        pass

    def validation(self):
        pass
  
class DataFramer(Command):
    
    def __init__(self, ip, port):
        self.ip = ip_addr
        self.port = port_number
        self.buffer = None
        self.client = None
        """
        self.header = {
            'operand' : None,
            'factoryCode' : None,
            'chimneyCode' : None,
            'length' : None,
            'startedAt' : None,
        }
        """
        self.header = []
        self.body = []
        self.tailor = []
        if self.client == None:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((ip_addr, port_number))
                self.client = client
            except Exception as e:
                print(traceback.format_exc())
        else:
            pass
        self.oper = None
        self.oper_leng = 4

    def validation(self):
        pass

    def send(self):
        pass

    def making_ascii(self, buffer):
        tmp_list = []
        for idx in range(len(buffer)):
            tmp_list.append(ord(buffer[idx]))
        
        return tmp_list

class DataGather(DataFramer):

    """ 
    this class will detecting header & do some needed logic

    """
    def devide_header(self):
        self.oper = self.get_operands()
        if self.oper == None:
            raise Exception
        else:
            pass
    #헤더를 구분한다.

    def get_data_recv(self):
        self.buffer = self.client.recv(1024)
        return self.buffer

    def data_length(self, code):
        return len(code)
    #명령어의 특정 부분 파싱해서 길이 확인 -> vaildation check에 활용 될 예정임.

    def validation(self):
        if self.oper in operands:
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
        return operands.decode(encoding = encoding) #str 'TDAT' return

    def check_crc(self, data):
        pass

    def resent_buffer(self):
        self.buffer = None

    def message(self):
        msg = "테스트용 메시지 입니다."
        return msg #string 형태로 return?


""" 위 클래스는 -> 새로운 클래스로 만들어서, 팩토리에서 쓰일 것에 기본 틀로 상속해야 할듯. 여기있으면 안됨 """


class PDUM(DataFramer):
    def __init__(self):
        pass

    def send(self):
        print("PDUM")

class TDAT(DataFramer):
    def __init__(self, *args):
        super().__init__(ip_addr, port_number)

    def making_header(self):
        tmp_buf = []
        tmp_text = ''
        header = {
            'operand' : 'TDAT',
            'factoryCode' : factoryCode,
            'chimneyCode' : chimeyCode,
            'length' : self.check_code_length(),
            'startedAt' : DATETIME #this should be changed
        }
        for k, v in enumerate(header):
            tmp_buf.append(v)
        for i in tmp_buf:
            tmp_text += i
        self.header = self.making_ascii(tmp_text)
        print('this is header' , self.header)

    def making_body(self):
        #TODO: list up what should be in body
        #바디의 길이는 명령어에 따라서 가변이다.
        tmp_buf = []
        tmp_text = ''
        body = {
            'countData' : response['countData'],
            'payload' : response['payload']
        }
        for k,v in enumerate(body):
            tmp_buf.append(v)
        for i in tmp_buf:
            tmp_text += i
        self.body = self.making_ascii(tmp_text)
    
    def making_tail(self):
        #TODO: check crc tailor logic
        pass

    def check_code_length(self):
        return len(self.header + self.body + self.tailor)
    #TODO: before making all code, do check header + body + tail legnth & put is in the header

    def making_binary_code(self):
        self.making_header()
        self.making_body()
        self.making_tail()
        struct_fmt = '={}b'.format(self.check_code_length()) #struct to binary
        binary_data = struct.pack(struct_fmt, *(self.header + self.body)) 
        return binary_data
        #TODO: making this code as binary code ! with struct.pack !! above is tmp

    def validation(self):
        #TODO: add 
        # logic to check all code is right -> only True send logic will execute
        return True

    def send_to_server(self, data):
        #서버에 올리기위한 로직을 구현해야한다.
        try:
            self.client.sendall(data) #커넥션 맺은 ip, port로 바이너리 데이터 전송.
        except Exception as e:
            print(traceback.format_exc())


    def send(self):
        self.making_header()
        self.making_body()
        self.making_tail()
        binary_data = self.making_binary_code()

        self.send_to_server(binary_data)

        #생성된 헤더+바디+테일을 바이너리 데이터로 말아서 환경부 서버에 올리는 로직 구현 해야 함.



if __name__ == "__main__":
    data_gather = DataGather(ip_addr, port_number)
    data_gather.get_operands()
    #Command.factory('TDAT').do()
    DataGather.factory('TDAT').do()