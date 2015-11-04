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
print >>sys.stderr, "connecting to %s port %s" % server_address

sock.connect(server_address)

try:
	message = "This is the message that'll be repeated."
	print >>sys.stderr, "sending '%s'" % message

	sock.sendall(message)

	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print >>sys.stderr, "receiving '%s'" % data

finally:
	print >>sys.stderr, "closing socket."
	sock.close()