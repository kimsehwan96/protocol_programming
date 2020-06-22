import abc
import traceback
import time
import datetime
import socket

#데이터 처리는 hex ascii로. byte로 받은 데이터를 ascii -> hex로 변환.

ip_addr = '127.0.0.1'
port = 9999

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP connections
sk.connect((ip_addr, port))

command = {
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


class ReceiveCmd(Command):
    def send(self):
        pass

    def validation(self):
        pass


"""
below objects are describing what process sholud be done in specific command.
"""

class PDUM(ReceiveCmd):
    def __init__(self):
        pass

    def send(self):
        print("PDUM")

class PDUM2(ReceiveCmd):
    def __init__(self):
        pass

    def send(self):
        print("PDUM2")


Command.factory("PDUM").do()
