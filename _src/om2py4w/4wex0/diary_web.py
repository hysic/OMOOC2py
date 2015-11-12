# -*- coding: utf-8 -*-
#! /usr/bin/env python

__author__ = "hysic"
__mail__ = "hysic1986@gmail.com"

from bottle import route, request, template, run, debug
import time
from os.path import exists

filename = 'diary.log'

if not exists(filename):
	with open(filename, 'a'):
		pass

@route('/diary')
def show_diary():
	return template("write_diary.tpl", diary_file=filename)

@route('/diary', method='POST')
def write_diary():
	new_line = request.POST.get('new_line', '')

	if new_line == 'clear':
		with open(filename, 'w') as f:
			pass
	else:
		with open(filename, 'a') as f:
			current_time = time.strftime("%Y-%m-%d %H: %M: %S")
			diary_content = current_time + '\t' + new_line + '\n'
			f.write(diary_content)

	return template("write_diary.tpl", diary_file = filename)


if __name__ == "__main__":
	#debug(True)
	#run(host='localhost', port=8080, reloader=True)
	run(host='localhost', port=8080)