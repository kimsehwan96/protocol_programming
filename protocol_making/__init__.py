from interfaces import BaseFramer

class Framer(BaseFramer):

    def sendPacket(self, message):

        return self.client.send(message)
    
    def recvPacket(self, size):

        return self.client.recv(size)