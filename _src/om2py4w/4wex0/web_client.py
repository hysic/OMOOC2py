# -*- coding: utf-8 -*-
#! /usr/bin/env python

__author__ = "hysic"
__mail__ = "hysic1986@gmail.com"

import requests
from lxml import html

help_message = """欢迎来到小小日记系统 Web 版
	type h/help/? for help
	type q/quit to quit
	type r/sync to show history

	ATTENTION: type clear to empty history!!!
	"""


server_address = 'http://localhost:8080/diary'

def read_diary():
	# get the request data from the server page
	r = requests.get(server_address)
	# parse the page content into a nice tree structure
	tree = html.fromstring(r.content)
	# use XPath to get to the html section you want
	diary_content = tree.xpath('//div[@id="diary_content"]/p/text()')

	return diary_content


def write_diary(diary_note):
	rw = requests.post(server_address, data = {'new_line': diary_note})

	print "%s have been sent to the web server." % diary_note



def main():
	while True:
		diary_note = raw_input('>>> ')
		if diary_note in ['h', 'help', '?']:
			print help_message
		elif diary_note in ['q', 'quit']:
			print "Bye ~"
			break
		elif diary_note in ['r', 'sync']:
			for line in read_diary():
				print line
		else:
			write_diary(diary_note)

if __name__ == "__main__":
	main()