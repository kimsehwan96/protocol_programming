from util import BaseClass
import struct
import datetime
import time
import traceback

#헤더의 총 길이는 28바이트
class Header(BaseClass):

    def __init__(self, buffer):
        self.struct_fmt = '=28b'
        self.struct_len = struct.calcsize(self.struct_fmt)

        if buffer != None:
            unpacked = struct.unpack(self.struct_fmt, buffer)
            self._header = {
                'operand' : unpacked[0:4],
                'factory_code' : unpacked[4:11],
                'chimney_code' : unpacked[11:14],
                'msg_length' : unpacked[14:18],
                'check_time' : unpacked[18:28]
            }
            self.operand = unpacked[0:4] #4바이트
            self.factory_code = unpacked[4:11] #7바이트
            self.chimney_code = unpacked[11:14] #3바이트
            self.msg_length = unpacked[14:18] #4바이트
            self.check_time = unpacked[18:28] #10바이트
            self.all_code = unpacked
            print(unpacked)
            print(len(unpacked))
        else:
            pass
        #TODO : if data is not in buffer async process will do.

    def check_frame(self, buffer):
        pass

    def GetBytes(self):
        return struct.pack(
            self.struct_fmt,
            """
            *(
                *self.operand,
                *self.factory_code,
                *self.chimney_code,
                *self.msg_length,
                *self.check_time
            )
            """
            *self.all_code
        )
    
    def GetSize(self):
        print(self.struct_len)
        return self.struct_len
    
    def making_code(self, code: tuple):
        str_object = ''
        for i in code:
            str_object += chr(i)
        return str_object
    
    def GetHex(self):
        hex_list = []
        for i in self.all_code:
            hex_list.append(hex(i))
        print(hex_list)
        return hex_list #returing list of hex

class Body(BaseClass):
    def __init__(self, buffer):
        pass





if __name__ == '__main__':
    #msg = 'TDAT123456712312341234567890'
    msg = 'TDAT1200001001  582002251300'
    msg_ord = []
    for i in msg:
        msg_ord.append(ord(i))
    
    buffer = struct.pack('=28b', *msg_ord)
    print("this is buffer {}".format(buffer))
    h = Header(buffer)
    print(h.GetBytes())
    print(h.GetSize())
    print(h.making_code(h.operand))
    h.GetHex()

        

"""
헤더 구조 

4바이트 , 7바이트, 3바이크 , 4바이트 , 10바이트. 부호코드는 hex ascii
총 헤더 길이는 28바이트

"""