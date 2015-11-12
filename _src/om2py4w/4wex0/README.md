# 日记系统 Web 版使用说明

~ 系统: OS X 10.10
~ python 版本: 2.7.10
~ 第三方库: 
	
* 服务器: [bottle](http://bottlepy.org/docs/dev/index.html)
* CLI客户端: [requests](http://docs.python-requests.org/en/latest/), [lxml](http://lxml.de/)

~ 代码地址: <https://github.com/hysic/OMOOC2py/tree/master/_src/om2py4w/4wex0>

* 代码说明
	+ 命令行进入当前代码目录, 安装 `bottle` 模块, `python diary_web.py` 启动 Web 服务器.
	+ 任意浏览器地址栏输入 `127.0.0.1:8080/diary` 即可进入网页, 在输入框中输入任何文字, 回车保存. 再次进入会显示历史记录.
	+ 安装 `requests` 和 `lxml` 模块, `python web_client.py` 启动 CLI 客户端, 输入任何文字, 回车即可发送值服务器, 输入 h/help/? 显示帮助, 输入 r_sync 显示历史, 输入 q/quit 退出客户端.
	+ 注意: 网页版和 CLI 版中, 输入 clear 可以清空历史记录, 慎用!!!


