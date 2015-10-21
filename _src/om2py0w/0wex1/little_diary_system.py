# -*- coding: utf-8 -*-

## Filename: little_diary_system.py
## Author: hysic1986
## Date created: 2015.10.12
## Date late modified: 2015.10.21
## Python Version: 2.7

import sys
import os
import time

def main():
	#script, txt = sys.argv
	print "Little Diary System v0.1"

	file_name = "dairy.txt"
	dairy_file = open(file_name, "a+")

	# 判断文件是否为空
	# 若不为空, 打印其内容到屏幕
	if os.stat(file_name).st_size != 0:
		print "==========过往日记内容=========="
		dairy_file.seek(0)
		print dairy_file.read()
		print "==========日记内容结束=========="

	print "请输入新的日记内容, 按 enter 换行, 按 control-C 或 control-D 终止输入"

	while True:
		try:
			content = raw_input("> ")
			t_list = time.ctime().split()
			#dairy_file.write(t_list[-1] + '-' + t_list[1] + '-' + t_list[2] + ' ' + t_list[3] + '\t')
			dairy_file.write(time.ctime() + '\t')
			dairy_file.write(content)
			dairy_file.write("\n")

		except (KeyboardInterrupt, EOFError):
			dairy_file.close()
			sys.exit("退出日记.")	

if __name__ == "__main__":
	main()