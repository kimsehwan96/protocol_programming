import os
import sys
from bluetooth import *
from uuid import *
import find_dev


def recv_msg(ADDR):
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    print("Now we will try to connect to ADDR {}".format(ADDR))

    server_sock = BluetoothSocket( RFCOMM )
    server_sock.bind((ADDR, PORT_ANY))
    server_sock.listen()

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
    target_address = find_dev.find_device(sys.argv[1])
    recv_msg(target_address)
