# -*- coding: utf-8 -*-
#! /usr/bin/env python

__author__ = "hysic"
__mail__ = "hysic1986@gmail.com"

import socket

print """欢迎来到小小日记系统 Net 版
	type h/help/? for help
	type q/quit to quit
	type r/sync to show history"""

server_address = ('localhost', 10001)

# create an client socket, using UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


with open("google.pdf", "rb") as f:
	for line in f.read():
		sent = sock.sendto(line, server_address)

		print "sending %s bytes to '%s'" % (sent, server_address[0])

sock.close()