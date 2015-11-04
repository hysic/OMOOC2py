# -*- coding: utf-8 -*-
#! /usr/bin/env python
'''
文件说明
作者信息
版本自述
...
'''

from socket import *
import sys

sock = socket(AF_INET, SOCK_STREAM)

server_address = ('localhost', 10001)
print >>sys.stderr, "Starting up on %s port %s" % server_address

sock.bind(server_address)

sock.listen(1)

while True:
    print >>sys.stderr, "Waiting for a connection"
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, "Connection from", client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, "received '%s'" % data
            if data:
                print >>sys.stderr, "sending back to the client"
                connection.sendall(data)
            else:
                print >>sys.stderr, "no more data from", client_address
                break
    finally:
        connection.close()
