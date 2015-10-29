# 小小日记系统 GUI 版开发记录

~ 任务需求:

> + 每次运行时合理的打印出过往的所有笔记
> + 一次接收输入一行笔记
> + 保存为本地文件

~ 代码: <https://github.com/hysic/OMOOC2py/blob/master/_src/om2py0w/0wex2/diary_gui.py>
~ 代码说明: <https://github.com/hysic/OMOOC2py/tree/master/_src/om2py0w/0wex2>

## 啥是 Tkinter?
* 对于小白来说, 我认为[官方文档](https://docs.python.org/2.7/library/tkinter.html)并不是一个很好的入门教程, 通篇只有4个 Demo 实例, 而且还没有给运行效果图.
* 我的理想教程应该是由简入繁, 开始不要讲底层代码的事情, 给段代码给个效果, 然后再一步步完善.
* 我主要是通过这两个教程对 Tkinter 有了一个初步的了解:
  * [Python Tkinter](http://www.python-course.eu/python_tkinter.php)
  * [Python GUI Programming (Tkinter)](http://www.tutorialspoint.com/python/python_gui_programming.htm)

## 布局思路
* 顶端三个按钮(三个 Button widget, 包括在以个 Frame widget 内)
  * History: 显示历史记录
  * Clear: 清空所有记录
  * Close: 关闭窗口
  * 由于是自动保存, 所以并没有设置保存按钮
* 文字展示区域(Text widget)
  * 显示历史记录, 以及一些提示信息
  * 显示刚输入的文字
* 文字输入区域(Entry widget)

## Entry widget 中文输入问题

### What
* Entry widget中无法输入中文, 在`E.get()`后增加`.encode("utf-8")`后, 可以复制中文到文本框, 但无法用中文输入法输入

### How
* 所有搜索都指向 Python 官网的[这个链接](https://www.python.org/download/mac/tcltk/), 后来发现大妈早已在芝麻星中给出了这个参考链接(视而不见)
* 这个链接说要更新 Tcl/Tk 版本, 好, 那就更新吧, 下载安装了ActiveTcl 8.5.18.0, 终端中输入`wish`, 提示版本为`Tcl 8.5 & Tk 8.5 (8.5.18)`, 安装成功了
* 重新运行 python 脚本, 还是输入不了中文, 郁闷 ing
* 发现 Issue 中已经有小伙伴提了[这个问题](https://github.com/OpenMindClub/OMOOC2py/issues/54), 大妈也回复了, 经典的连珠七连问
* 还是不明白, 又看了一遍上面的官网链接, 发现这样一句话

> The Tcl/Tk major version is determined when the installer is created and cannot be overridden.

* 这意思是我重新装一个 python 就可以了么? 果断去官网重新下了一个2.7.10, 运行`python diary_gui.py`, 哦耶, 可以输入中文了!!!

### Why
* 我之前用的一直是 mac 自带的 python, 版本 2.7.6, 位置 `/ usr/bin/python`, 新装的 python 版本 2.7.10, 位置 `/usr/local/bin/python`
* `type -a wish` 发现 `wish` 也有两个版本, 一个是系统自带的 8.5.9 版本位于 `/usr/bin/wish`, 链接位置在`/System/Library/Frameworks/Tk.framework/Versions/8.5/Resources/Wish.app/Contents/MacOS/Wish"`, 另一个是新装的 8.5.18 版本位于 `/usr/local/bin/wish`, 连接位置在`/Library/Frameworks/Tk.framework/Versions/8.5/Resources/Wish.app/Contents/MacOS/Wish`. 
* python2 首次 `import Tkinter` 时, 先在 `/Library/Frameworks` 中查找 Tcl/Tk 框架, 找不到的再去 `/System/Library/Frameworks` 中查找.
* ipython 对应的 python 版本可以打开 `/usr/local/bin/ipython`, 将第一行改成自己需要用的 python 版本所在的位置即可.(参考 <http://stackoverflow.com/questions/9386048/ipython-reads-wrong-python-version>)

### 未解问题
~ 目前已经能在 Entry widget 中正常输入中文了, 但还是对大妈的七连问中这个问题不太清楚:

* 如何令 Python 用相同的 Tkinter 调用不同的 Tk 版本? 
	* 初步思路是让 `/usr/local/bin/wish` 链接到不同的 Tcl/Tk 版本中

## 进一步工作
* 在文本显示区域增加滚动条(ScrollBar)
* 界面美化
* 界面友好??
* ipython notebook 版本??


