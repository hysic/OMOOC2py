# 日记系统 net 版

~ 任务需求
>* 每次运行时合理的打印出过往的所有笔记
>* 一次接收输入一行笔记
>* 在服务端保存为文件:
>   * 在所有访问的客户端可以获得历史笔记
>* 支持多个客户端同时进行笔记记录

## 任务开发记录
* [socket 模块官方文档](https://docs.python.org/2/library/socket.html)看的一头雾水, 对于我这样对 socket 没有基本常识的小白来说,通读一遍基本是一头雾水, 只好暂且放下, 留待后面查看.
* google `python socket udp`, 找到python wiki 中的 [UDP Communication](https://wiki.python.org/moin/UdpCommunication), 以及PyMOTW 上的[User Datagram Client and Server](https://pymotw.com/2/socket/udp.html), 二者的优点都是提供了一个创建 UDP server 和 client 的最小脚手架, 可以在此基础上添加自己需要的功能.
* 我主要以PyMOTW 上的[User Datagram Client and Server](https://pymotw.com/2/socket/udp.html)为脚手架完成本周的任务.
	* server 端

	```python
	import socket

	# create a UDP server socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# bind the socket to the server address
	server_address = ('localhost', 10001)
	sock.bind(server_address)

	# receive the data and the client address
	data, client_address = sock.recvfrom(1024)
	```

	* client 端

	```python
	import socket

	# create a UDP client socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	server_address = ('localhost', 10001)
	message = 'This is the message.'

	# send the message to the server
	sent = sock.sendto(message, server_address)
	
	# close the socket
	sock.close()
	```
	
* 如此即可完成 server 和 client 之间的一次数据传送, 接下来以此为基础, 增加任务需求功能.
	> 每次运行时合理的打印出过往的所有笔记
	
	+ 相当于从 server 端向 client 端传送数据, 在 server 端已经获取到 client_address, 只需要在 server 端增加 `sent = sock.sendto(message, client_address)` , client 端增加 `data, server = sock.recvfrom(1024)` .
	
	
	> 一次接收输入一行笔记
	
	+ client 端增加 `while True` 无限循环, 利用`raw_input()` 函数提示用户输入.

	> 在服务端保存为文件
	> 在所有访问的客户端可以获得历史笔记
	
	+ 这与前两周的任务要求并无二致, 文件基本读写操作, 采用 `with open("diary.log", "a+") as f:`, 输入一行保存一行.

	> 支持多个客户端同时进行笔记记录
	
	+ 这似乎是 UDP 协议的特性, 

* 接下来就是在 client 端增加一些默认参数, h/help/? 显示帮助, r/sync 显示历史记录, q/quit 退出 socket.然后用  `if/elif/else` 语句进行条件判断.
* 具体代码见: <>, 代码运行说明见: <>.
* 任务需求的功能基本实现了, 下面看看任务代码具体是什么意思.

## 啥是 socket?
`sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`

* python 中 socket 对象初始化时有两个参数, 第一个是 `address famlily`, 用来声明 [OSI 模型](https://en.wikipedia.org/wiki/OSI_model)中网络层的协议, 常见的就是 `AF_INET`, 即为 IPv4; 第二个是 `socket type`, 用来声明 OSI 模型中传输层的协议, 常见的有两种, `SOCK_DGRAM` 用于 UDP 协议, `SOCK_STREAM` 用于 TCP 协议.
*  socket 是计算机进程间通信(IPC)的一种(其他的还有??), 可以跨操作系统. 比如现在绝大部分计算机之间通过 IP 协议互相通信, 因此绝大部分 socket 都是 Internet Socket. 
* socket 翻译成汉语为插座, 在计算机领域翻译成**套接字**, 根据知乎的启发, 参见[socket pipe 的 google 图片搜索](https://www.google.co.jp/search?q=socket+pipe&es_sm=119&tbm=isch&tbo=u&source=univ&sa=X&ved=0CBwQsARqFQoTCNjLmvD59cgCFcqflAodOu0HoA&biw=1373&bih=782#), 可以对 socket 的接口作用有一个直观地理解.

## 啥是 C/S 架构?
* Client/Server 架构(主从式架构), 是一种常见的软件架构模型, 我们日常所接触的网络基本都是 C/S 架构的, 如互联网, E-mail, 网络游戏, 微信.
* 与之相对的结构方式为 P2P(peer-to-peer)架构.
* server 端的 socket 对象需要绑定(bind)一个 socket 地址. 一个 socket 地址包括一个 IP 地址和一个端口号(port number). 比如运行下面的代码:

  ```python
  import socket
  print socket.getaddrinfo("www.python.org", "http")
  ```
  即可得到
  
  ```
  [(2, 2, 17, '', ('103.245.222.223', 80)),
 (2, 1, 6, '', ('103.245.222.223', 80))]
  ```
   ('103.245.222.223', 80)就是 HTTP 连接 python 官网的 socket 地址. 

## 啥是 UDP?
> 用户数据报协议（英语：User Datagram Protocol，缩写为 UDP），是一个简单的面向数据报的传输层协议，正式规范为 RFC 768.
> UDP只提供数据的不可靠传递，它一旦把应用程序发给网络层的数据发送出去，就不保留数据备份.

* [UDP vs TCP](http://www.cyberciti.biz/faq/key-differences-between-tcp-and-udp-protocols/)
	+ TCP 更加可靠, 不会丢失数据, 数据是顺序传输的; 
	  UDP 更加快速, 支持, 允许丢包和乱序.

	+ TCP server 端需要先建立 socket, 然后 bind → listen → accept 一系列操作, 才能和客户端发送/接收数据;
	  client 端需要先建立 socket, 然后 connect 到制定 socket 地址, 才能和服务器端发送/接收数据.
	  发送/接收数据采用 send/recv 方法.
	![TCP 流程图](https://upload.wikimedia.org/wikipedia/commons/a/a1/InternetSocketBasicDiagram_zhtw.png)
	+ UDP server 端建立 socket, 与 server 地址绑定(bind)后即可与客户端发送/接收数据.
	  client 端只需建立 socket 即可与服务器发送/接收数据.
	  发送/接收数据采用 sendto/recvfrom 方法, sendto 需制定 socket 地址.
* UDP 传输何种情况下会丢包或乱序??
	* 我本地传送了一个 pdf 文件, 将其作为二进制文件打开, 然后传输, 传输结果目测没有任何问题. (我相当于花了十几分钟完成了一个9MB pdf 的复制)

## 进一步任务
* 保存笔记的客户端来源? 并输出不同客户端提交的笔记?
* multicasting??

