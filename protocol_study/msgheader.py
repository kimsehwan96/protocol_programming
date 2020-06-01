from util import ISerializable
import struct

class Header(ISerializable):

    def __init__(self, buffer):
        self.struct_fmt = '=3I2BH' #3 uint, 2byte, 1 ushort
        self.struct_len = struct.calcsize(self.struct_fmt)

        if buffer != None:
            unpacked = struct.unpack(self.struct_fmt, buffer)

            self.MSGID = unpacked[0]
            self.MSGTYPE = unpacked[1]
            self.BODYLEN = unpacked[2]
            self.FRAGMENTED = unpacked[3]
            self.LASTMSG = unpacked[3]
            self.SEQ = unpacked[5]

    def GetBytes(self):
        return struct.pack(
            self.struct_fmt,
            *(
                self.MSGID,
                self.MSGTYPE,
                self.BODYLEN,
                self.FRAGMENTED,
                self.LASTMSG,
                self.SEQ
            )
        )

    def GetSize(self):
        return self.struct_len