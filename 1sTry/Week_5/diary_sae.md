# 日记系统公网(SAE)版
~ 任务需求
>* 将上周应用网站发布为公网稳定服务, 可以通过固定域名访问系统:
>	* 每次运行时合理的打印出过往的所有笔记
>	* 一次接收输入一行笔记
>	* 在服务端保存为文件
>	* 同时兼容 3w 的 Net 版本的命令行界面进行交互
>* 可以通过本地命令行工具监察/管理网站:
>	* 获得当前笔记数量/访问数量等等基础数据
>	* 可以获得所有笔记备份的归档下载

## 任务开发记录
### SAE 介绍
* [PAAS vs VPS](https://www.quora.com/Should-I-choose-a-VPS-or-a-PAAS-How-to-make-that-decision)
* SAE(Sina App Engine), 新浪应用引擎平台, 就是它给你提供服务器和运行环境, 你只要把你的代码传上去, 它就帮助你的应用运行和维护. 大名鼎鼎的[乌云](http://www.sinacloud.com/index/typical_detail/other/37.html)也是托管在 SAE 上的.
* 一个应用目录下至少要有两个基本文件
	* 一个是 `config.yaml`, 内容如下:

		```
		name: hysic's Diary
		version: 2
		```
	
	* 另一个是 `index.wsgi`, 替换之前的`.py`文件. 例如使用 Bottle 框架的 HelloWorld 例子如下:
	  
	  ```python
	  from bottle import Bottle, run
	  import sae
	  
	  app = Bottle()
	  
	  @app.route('/')
	  def hello():
	      return "Hello, world! - Bottle"
	      
	  application = sae.create_wsgi_app(app)
		```

* 当然, 你无须每次都本地写好代码, 然后上传 SAE 看效果, SAE 支持本地开发, python 可以本地安装 `pip install sae-python-dev`, 然后进入 `index.wsgi` 所在目录, 运行 `dev_server.py`, 进入 `http://localhost:8080` 即可本地查看效果. 
* 然后就是上传到 SAE 服务器端, git 或 svn 均可, 还是用我们熟悉的 git.
	
	```shell
	git init
	git add sae https://git.sinacloud.com/hysic1986
	git add --all
	git commit -m "first commit"
	git push sae master:1
	```

#### KVDB
* SAE 有一套自己的数据库, 就叫 KVDB, 和他家"weibo牌微博"有的一拼.
* KVDB 的 API 只有几个函数, 参考[官方说明](http://www.sinacloud.com/doc/sae/python/kvdb.html)很容易理解.
* 数据库的 key 主要设置了这几个:
	* "diary_num": 记录日记数量
	* "access_num": 记录访客数量
	* "note"+数字n: 第 n 条日记, 格式为 `{"time": current_time, "content": new_line, "tag": tag}`
	* "tag": 标签dict, key 是标签, value 是相应标签的日记


### UI 设计
* 理想状态: google "diary tag" 发现了iOS 应用[Tag Journal](https://itunes.apple.com/us/app/tag-journal-write-your-diary/id742204884?mt=8), 界面很好看.
* 目前状态: 导航栏, 左侧边栏(显示 tags), 提示输入框, 历史日记显示, footer(显示日记数量及访客数量).

![](https://github.com/hysic/OMOOC2py/blob/master/1sTry/Week_5/sae-UI.png?raw=true)

* 坑: 本地测试左侧 tag 边栏显示 OK, 上传 SAE 后无法显示.

### CLI 交互
* CLI 访问类似上周的任务, 只是服务器地址由 `localhost` 变成 `http://hysic1986.sinaapp.com`, 需要的模块有 `requests` 和 `lxml`.
* 需要的功能包括: 读日记, 写日记, 读取笔记数量, 读取访问数量, 清空日记及统计.


### 遗留问题
* api 设计?? e.g. 清空日记
* 界面设计??
* 代码越来越复杂, 如何简化或调试??
* 本地测试 边栏tag显示 ok, 上传 sae 无效??


