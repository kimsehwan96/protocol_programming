import struct
from six import byte2int


def convert_hex(buffer: list):
    l = []
    for idx in buffer:
        l.append(hex(idx))
    return l #list return


def __generate_crc16_table():
    result = []
    for byte in range(256):
        crc = 0x0000
        for _ in range(8):
            if (byte ^ crc) & 0x0001:
                crc = (crc >> 1) ^ 0xa001
            else: crc >>= 1
            byte >>= 1
        result.append(hex(crc))
    return result

def computeCRC(data):

    crc = 0xffff
    for a in data:
        idx = __crc16_table[(crc ^ byte2int(a)) & 0xff]
        crc = ((crc >> 8) & 0xff) ^ idx
    swapped = ((crc << 8) & 0xff00) | ((crc >> 8 ) & 0x00ff)
    return swapped


def checkCRC(data, check):
    return computeCRC(data) == check
    

__crc16_table = __generate_crc16_table()
