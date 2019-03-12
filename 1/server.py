# Server

import socket
import time
import sys


def tcpStreamingServer():
    HOST = 'localhost'
    PORT = 9876
    ADDR = (HOST, PORT)
    BUFF_SIZE = 1024 * 1024

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(ADDR)
    serv.listen(5)

    print 'listening ...'

    while True:
        conn, addr = serv.accept()
        print 'client connected ... ', addr

        cntMessages, cntBytesRead = 0, 0
        startTime = time.time()
        while True:
            data = conn.recv(BUFF_SIZE)
            if not data:
                break
            cntMessages += 1
            cntBytesRead += len(data)
            print cntMessages, cntBytesRead

    conn.close()
    finishTime = time.time()
    print 'client disconnected'
    print '# Messages: %d' % cntMessages
    print '# Bytes Read: %d' % cntBytesRead
    print 'Time spent: %d sec' % (finishTime - startTime)


def udpStopAndWaitServer():
    HOST = 'localhost'
    MY_PORT = 9876
    ADDR = (HOST, MY_PORT)
    BUFF_SIZE = 1024
    serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serv.bind(ADDR)
    cntMessages, cntBytesRead = 0, 0
    startTime = time.time()
    while True:
        #print 1
        data, clientAddr = serv.recvfrom(BUFF_SIZE)
        #print 2
        if not data or (len(data) == 10 and data.decode() == 'force_exit'):
            break
        serv.sendto(str(cntMessages).encode(), clientAddr)  # sending ack
        #print 3
        cntMessages += 1
        cntBytesRead += len(data)
    finishTime = time.time()
    print 'client disconnected'
    print '# Messages: %d' % cntMessages
    print '# Bytes Read: %d' % cntBytesRead
    print 'Time spent: %d sec' % (finishTime - startTime)


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1].lower() == 'tcp':
        tcpStreamingServer()
    else:
udpStopAndWaitServer()
