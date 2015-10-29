# -*- coding: utf-8 -*-
#! /usr/bin/env python
'''


'''

from Tkinter import *
import time
from os.path import exists

# 日记文件
diary_file = "diary.log"


def main():
	# GUI 主窗口
	root = Tk()
	root.title("Little Diary")
	root.geometry("600x400+0+0")

	# 显示历史记录
	def showHistory():
		if exists(diary_file):
			diary = open(diary_file, "r")
			T.delete(1.0, END)
			T.insert(END, "="*9+"过往日记内容"+"="*9+'\n')
			T.insert(END, diary.read())	
			T.insert(END, "="*9+"日记内容结束"+"="*9+'\n')
			diary.close()
		else:
			T.insert(END, "Sorry, 没有找到日记文件, 现在开始记录吧.\n")

	# 清空日记内容
	def clearDiary():
		if exists(diary_file):
			open(diary_file, "w").close()
			T.insert(END, "日记文件内容已清空.\n")
		else:
			T.insert(END, "日记文件不存在. 现在开始记录吧.\n")

	# 增加一行日记
	def addLine(event):
		# add line in diary_file
		diary = open(diary_file, 'a')
		new_line = E.get().encode("utf-8")
		current_time = time.strftime("%Y-%m-%d %H: %M: %S")
		diary.write(current_time + '\t')
		diary.write(new_line + '\n')
		diary.close()
		E.delete(0, END)

		# add line in Text Widget
		T.insert(END, new_line)


	frm = Frame(root, height = 10)
	frm.pack()

	button1 = Button(frm, text="History", width = 20, command = showHistory)
	button1.pack(side = "left", padx = 5, pady = 2)

	button2 = Button(frm, text = "Clear", width = 20, command = clearDiary)
	button2.pack(side = "left", padx = 5, pady = 2)

	button3 = Button(frm, text="Close", width = 20, command = root.destroy)
	button3.pack(side = "left", padx = 5, pady = 2)


	T = Text(root, height = 15, bg = "#dfd", font = "Arial 14")
	T.pack()
	# add ScrollBar

	frm2 = Frame(root, height = 10)
	frm2.pack()

	L = Label(frm2, text = "请输入一行日记 >>> ")
	L.pack(side="left")

	E = Entry(frm2, width = 50)
	E.pack(side="left")
	E.bind("<Return>", addLine)

	root.mainloop()


if __name__ == "__main__":
	main()