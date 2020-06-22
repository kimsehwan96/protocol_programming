import abc
import traceback
import time
import datetime
import socket

#데이터 처리는 hex ascii로. byte로 받은 데이터를 ascii -> hex로 변환.

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

class Command:

    __metaclass__ = abc.ABCMeta

    def do(self):
        #if self.validation():
        #    self.send()
        #else:
        #    raise Exception
        self.validation()
        self.send()

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
아래 코드들은 명령어 (header + body + tailor 가 모두 수집되고, vaildation 체크가 끝났을 때 돌아야 하는 로직 임.)
즉 DataGather 클래스에서 모든 checking logic 통과 / header + body + tailor 나눈 뒤에, 해당 헤더 바디 테일을 보고 로직이 돌아야 함

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

class TDAT(ReceiveCmd):
    def __init__(self):
        pass

    def send(self):
        print("this oper is TDAT ! !")
        print("Parents class TDAT was executed!")


Command.factory("TDAT").do()
