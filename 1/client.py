# Client

import socket
import sys


def tcpStreamingClient():
    HOST = 'localhost'
    PORT = 9876
    ADDR = (HOST, PORT)
    BUFF_SIZE = 1024 * 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    with open("file.binary", "rb") as f:
        while True:
            chunk = f.read(BUFF_SIZE)
            if not chunk:
                break
            client.send(chunk)

    client.close()


def udpStopAndWaitClient():
    HOST = 'localhost'
    SERVER_PORT = 9876
    MY_PORT = 9877
    MY_ADDR = (HOST, MY_PORT)
    SERVER_ADDR = (HOST, SERVER_PORT)
    BUFF_SIZE = 1024

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind(MY_ADDR)

    with open("file.binary", "rb") as f:
        while True:
            chunk = f.read(BUFF_SIZE)
            if not chunk:
                break
            client.sendto(chunk, SERVER_ADDR)
            ack, _ = client.recvfrom(BUFF_SIZE)
    client.sendto("force_exit".encode(), SERVER_ADDR)
    client.close()


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1].lower() == 'tcp':
        tcpStreamingClient()
    else:
udpStopAndWaitClient()
