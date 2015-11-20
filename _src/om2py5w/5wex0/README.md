# 日记系统 SAE 版使用说明

* 系统: OS X 10.10 

* python 版本: 2.7.10 

* CLI客户端第三方库: [requests](http://docs.python-requests.org/en/latest/), [lxml](http://lxml.de/)

* SAE 网页地址: [hysic's Diary](http://hysic1986.sinaapp.com)

* 代码说明
	* 命令行进入当前代码目录, `python sae_client.py` 连接 SAE 服务器.
		* 输入 h/help/? 显示帮助信息
	   * 输入 r/sync 显示所有日记
    	* 输入 tag/Tag 显示所有标签
    	* 输入 # 显示统计信息(日记数量, 访客数量)
		* 输入 q/quit 退出
		* 输入其他内容将作为日记发送至服务器

