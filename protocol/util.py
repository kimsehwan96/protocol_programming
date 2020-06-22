import struct



def convert_hex(buffer: list):
    l = []
    for idx in buffer:
        l.append(hex(idx))
    return l #list return