import os
import sys
from bluetooth import *
from uuid import *
import find_dev


def recv_msg(ADDR):
    # 상대 기기의 uuid를 알아야 하나?
    uuid = "F749CD16-2AEB-C7B1-9A37-EE1776F7EA11"
    print("Now we will try to connect to ADDR {}".format(ADDR))

    server_sock = BluetoothSocket( RFCOMM )
    server_sock.bind((ADDR, PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    advertise_service(
        server_sock, "SampleServer", service_id = uuid,
        service_classes = [ uuid, SERIAL_PORT_CLASS ],
        profiles = [ SERIAL_PORT_PROFILE ] 
    )

    print("waiting for connection : ch {}".format(port))

    client_sock, client_info = server_sock.accept()
    print("accpet")

    while True:
        print("Accepted connection from, {}".format(client_info))
        try:
            data = client_sock.recv(1024)
            if len(data) == 0: break
            print("recieved {}".format(data))
        except IOError:
            print("disconnected")
            client_sock.close()
            server_sock.close()
            print("all doen")
            break
        except KeyboardInterrupt:
            print("disconnected")
            client_sock.close()
            server_sock.close()
            print("all doen")
            break

if __name__ == "__main__":
    target_address = sys.argv[1]
    target_address = find_dev.find_device(target_address)
    recv_msg(target_address)
