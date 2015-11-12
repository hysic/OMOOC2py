# 日记系统 Web 版

~ 任务需求
>* 通过网页访问系统:
>	* 每次运行时合理的打印出过往的所有笔记
>	* 一次接收输入一行笔记
>	* 在服务端保存为文件
>* 同时兼容 3w 的 Net 版本的命令行界面进行交互

~ 任务代码及说明: <https://github.com/hysic/OMOOC2py/tree/master/_src/om2py4w>

## 任务开发记录
### Bottle 框架
* 上下班路上通读[Bottle 官网 tutorial](http://bottlepy.org/docs/dev/tutorial.html), 只是对 bottle 的功能有个大概的印象, 但对本周作业如何实现依然没什么思路.
	* 直到我读到了官网上的这个 [Tutorial: Todo-List Application](http://bottlepy.org/docs/dev/tutorial_app.html)以及大妈的这个 [Simple-todo Bottle 实现版](https://bitbucket.org/ZoomQuiet/bottle-simple-todo/wiki/Home), 终于有了个模仿对象, 至少可以照葫芦画瓢完成任务了.
	* 说起官网文档看不懂的问题, 上次大妈也问过我这个问题. 我觉得是我的需求和官方文档不是一个思路. 我的需求是需要对小白从最基础的概念讲起, 每个概念都最好配上详细实例, 然后层层递进, 直至更复杂的实例. 而 Bottle 官网的 Tutorial 则力求做到面面俱到, 每一点特性都要顾及到, 反而没有什么重点. 对比下面用到的 `requests` 模块的[官方文档](http://docs.python-requests.org/en/latest/), 则比较对我的胃口, 显示 Quickstart, 帮助你快速上手, 然后是 Advanced Usage, 讲一些进阶用法, 适合于不同程度的用户. 所以我目前的看法是, 官方文档不可不看, 但若不对口味, 可以 google 寻找其他对口味的教程, 先入门了再说.
	* 现在再回头看[Bottle 官网 tutorial](http://bottlepy.org/docs/dev/tutorial.html), 对里面的一些术语有了基本的概念, 所以对里面的内容也有了更多地理解, 所以官方文档即使开始看不懂, 在其他地方入门了之后也一定要回读官方文档.

* Bottle 框架的几个函数
	~ 创建网页, 简单地说就是URL地址 + 网页内容(HTML+CSS+JS), 再就是与服务器的数据交互, Bottle 框架有几个函数分别做这几项事情.

	* `route` 路由, Bottle 中最重要的一个函数, 将 URL 与一个函数关联, 该函数的返回值则是这个 URL 对应网页的显示内容. 更重要的是, 这个 URL 可以是动态的, 可以用正则表达式涵盖好多类似的 URL 地址. `route` 还可以指定http 请求方法, 默认是 `GET`.

		```python
		@route('/diary')
		def show_diary():
			return template("write_diary.tpl", diary_file=filename)
		```
		
		比如这段代码对应的 URL 就是`/diary`, 网页显示的内容就是 `write_diary.tpl` 这个模板里面的内容.
		
	* `template` 模板, 将 html 分离成一个单独的文件, 可以多次使用, 可以缓存, 同时还可以传入一些需要修改的参数. Bottle 内置了 Simple Template 引擎, 足够完成本周任务. 大妈推荐的 `Jinja2` 模板引擎, 留待后续使用.
		
	```html
	<form action='/diary' method="POST">
		<input type="text" size="100" maxlength="100" name="new_line" autofocus>
		<input type="submit" name="save" value="保存">
	</form>

	<div id="diary_content">
	%with open(diary_file) as f:
		%for line in f:
			<p>{{line[0: -1]}}</p>
		%end
	%end
	</div>
	```
	
	这段代码就是我实现本周任务使用的模板, 注意到最后一个 `div` 里还有几行以`%`开头的 python 代码, 模板是允许这种写法的, 可以在模板内插入 `if`, `for` 等语句.
		
	* `request`, 用于服务器端和客户端之间交换数据, 比如 `new_line = request.POST.get('new_line', '')` 用于从网页中名为 `new_line` 的 input 元素中获取客户端的输入内容.

	* `run`, 服务器运行, 默认地址是 `localhost`, 默认端口是 `8080`. 添加 `reloader=True` 参数可以在在修改代码后不用重启服务器, 对调试代码很有用, 但在上线后一定要删除.
	* `debug`, 调试, 可以在网页端直接显示报错信息.

* 最终实现的网页界面是这样婶的.
![](/Users/hysic/python/OMOOC2py/_src/om2py4w/4wex0/webwebweb.png)


### CLI 交互
* 本周任务还有一个要求:

> 同时兼容 3w 的 Net 版本的命令行界面进行交互

* 我开始的想法是, 把3w client 端的代码直接拿来用. 创建一个 TCP socket, 连接 `localhost:8080/diary`, 然后 `recv` 数据, 可以毫无动静. 因为我服务器端并没有设置要向客户端 `send` 数据, 一切都是 bottle 封装好的 http 协议.
* 看了一下其他同学的代码, 发现 很多都用了 `requests` [模块](http://docs.python-requests.org/en/latest/), google 之, 很diao.

> Requests: HTTP for Humans

* 而且 requests 的文档写的比较符合我的胃口, [Quickstart](http://docs.python-requests.org/en/latest/user/quickstart/) 页面就满足了我的全部要求(读数据, 发送数据), 大赞!

```python
import requests
# get the request data from the server page
r = requests.get("127.0.0.1:8080/diary")
print r.content
# post data to the server
rw = requests.post("127.0.0.1:8080/diary", data = {'new_line': "some_message"})
```

* 这样输出的是包含 html 标签在内的全部网页内容, 需要进一步去除标签, 找到自己需要的那部分网页内容. google `python html`, 找到 Python Guide 的[这个页面](http://docs.python-guide.org/en/latest/scenarios/scrape/), 里面介绍了 `requests` 模块, 还有 `lxml` 模块, 刚好就是我需要的!! 而且, `lxml` 模块一共介绍了三行代码, 刚好可以完成我的要求, 太赞了!

```python
import requests
from lxml import html
# get the request data from the server page
r = requests.get(server_address)
# parse the page content into a nice tree structure
tree = html.fromstring(r.content)
# use XPath to get to the html section you want
diary_content = tree.xpath('//div[@id="diary_content"]/p/text()')
print diary_content
```

### 任务回顾
* 其实我感觉最大的难点不在代码本身, 而在于网站的架构, 需要有几个页面, 每个页面的 `get` 和 `post` 方法分别对应什么. 虽然最后只用了一个 URL, 但那是因为网站本身不复杂, 要是复杂一点, 比如做一个 todo list 网站, 就需要像大妈那样做 [URI 设计]((https://bitbucket.org/ZoomQuiet/bottle-simple-todo/wiki/HowThink))了.

## 下一步工作
* KVDB

* RESTful??


