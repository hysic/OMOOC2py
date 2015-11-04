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

while True:
	# prompt the user to input a line of note
	message = raw_input(">>> ")

	if message in ['help', 'h', '?']:
		print '''\
	type h/help/? for help
	type q/quit to quit
	type r/sync to show history'''

	elif message in ['q', 'quit']:
		print "close the client socket." 
		sock.close()
		break

	elif message in ['r', 'sync']:
		sent = sock.sendto(message, server_address)
		data, server = sock.recvfrom(1024)
		print "=" * 10 + "HISTORY" + "=" * 10
		print data
		print "=" * 10 + "HISTORY END" + "=" * 10

	else:
		# send the message to the server
		sent = sock.sendto(message, server_address)

		print "sending %s bytes to '%s'" % (sent, server_address[0])