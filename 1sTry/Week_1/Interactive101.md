# 极简日记系统

## 任务要求
> 完成一个极简交互式日记系统,需求如下:
> 
> * 一次接收输入一行日记
> * 保存为本地文件
> * 再次运行系统时,能打印出过往的所有日记

## 开发过程

~ 芝麻星中"第一周行动"卡包中已经将任务进行初步分解, 我主要按照分解的任务依次进行, 必要时做进一步任务分解.

### 脚本调用

  * 创建`.py`文件，每次在CLI中以`python main.py`运行之。

```
只有 .py 的文件才是我们应该持续修订的开发容器.
    ——ZoomQuiet
```

### 调用参数

  * 采用命令行参数([Command Line Arguments](https://docs.python.org/2/tutorial/stdlib.html#command-line-arguments))
  * `import sys`
  * 调用方法: `python main.py argv1 argv2 ...`
  * `main.py`是第一个参数
  * 参数个数与`main.py`中定义的个数相同, 参数过多或过少都会产生`ValueError`

### 输入中文

  * `python main.py 中文` 未出现异常.

### 持续交互

> 一次接收输入一行日记

  ~ 这里开始解决任务需求, 将任务需求进一步拆分. 
  ~ 这里需要解决两个问题, 一个是持续运行, 等待继续输入或退出; 一个是如何退出.
  
  * 持续运行
    * 不要每输入一句话都提示是否要继续
    * while True 循环
    * 注意一定要退出
  * 退出方式:
    * control-C control-D 退出
    * 注意: except KeyboardInterupt 之后一定要 break, 否则无法退出无限循环
    * sys.exit(exit_message), 无须 break
    * 小问题: `^C`
 
### 输出为文件

> 保存为本地文件

~ 这里可进一步拆分为文件打开, 文件读取, 文件读入, 文件保存关闭.
  
  * 文件打开
    * open(file_name, mode)
   * 文件读入
    * file.write(message)
    * 运行发现file.write并不会写入换行符
    * 注意要写入换行符'\n'
  * 文件关闭
    * file.close()
    * 一定要在退出前关闭文件
    * 不关闭会怎样?
    * 是否自动保存?
    
### 回读文本数据

> 再次运行系统时,能打印出过往的所有日记

~ 任务进一步分解: 确认文件内容不为空, 文件读取并print

  * 确认文件不为空
    * import os
    * os.stat(file_name).st_size != 0:
    * 参考: <http://stackoverflow.com/questions/2507808/python-how-to-check-file-empty-or-not>
    
  * 文件读取
    * f.read()
    * 以 a+ 方式打开的文件, 确认文件不为空后, 但 f.read()输出却为空
      * 以 a+ 方式打开的文件, file position(我理解为文件中的光标)位于文件末尾, 这样当然读不出东西来了
      * 使用 f.seek(0)将 file position 放在文件开头, 然后再 f.read()就行了 
      * 参考: <http://stackoverflow.com/questions/14639936/how-to-read-from-file-opened-in-a-mode>

### 增加时间
* 简单实现

	```python
	import time
	print time.asctime() # or time.ctime()
	```

	* 优点: 代码少
	* 缺点: 输出时间格式固定, 可用字符串拆分重组

## 开发心得
* 要努力克服完成一小步所产生的巨大的膨胀感, 以及由此产生的想关掉编辑器干点别的的念头
* @一休君所说的 <https://docs.python.org/2/index.html> 中的快速搜索框是个好东西.


## 下一步任务
- [ ] 任务中说"先不管数据结构", 这是什么意思?
- [ ] 中文编码问题?
- [ ] time 格式的定制输出, e.g. 2015-10-21 16:43
- [ ] DOCOPT的作用?


