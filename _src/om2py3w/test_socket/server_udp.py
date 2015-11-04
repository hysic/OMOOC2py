# -*- coding: utf-8 -*-
#! /usr/bin/env python

__author__ = "hysic"
__mail__ = "hysic1986@gmail.com"

import socket

server_address = ('localhost', 10001)

# create an server socket, using UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket the server address
sock.bind(server_address)

while True:
	print "Waiting to receive message."
	# receive the data and the client address
	data, client_address = sock.recvfrom(1024)

	print "received %s bytes from %s: " % (len(data), client_address)
	print data

	if data in ['r', 'sync']:
		with open("diary.log", 'r') as f:
			sent = sock.sendto(f.read(), client_address)
			print "sent %s bytes back to %s" % (sent, client_address)

	elif data:
		with open("diary.log", 'a') as f:
			f.write(data)
			f.write("\n")
		