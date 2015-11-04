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
	data, client_address = sock.recvfrom(4096)

	#print "received %s bytes from %s: " % (len(data), client_address)
	#print data

	with open("recv.pdf", 'ab') as f:
			f.write(data)
		