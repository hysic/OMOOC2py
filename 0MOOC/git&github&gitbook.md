# git 私人教程
issues
wiki

## 背景
很早就听说过github的大名（~~同性交友网站~~），在Coursera上某门MOOC也用过一点github，通读过[廖雪峰老师的git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000),但实际掌握的仅限于git基本操作，能向github push repo，没有进一步的需求也就没有进一步的动力。
## 需求
开智学院OMOOC2py课程主要依赖GitHub来完成，无论是任务发布还是技术问题讨论，这就有了进一步熟悉GitHub生态环境的必要与动力。

以开智学院[OMOOC2py仓库](https://github.com/OpenMindClub/OMOOC2py)为例，一进去是**code**标签，即代码仓库，可以fork到自己的仓库。右侧接下来是**Issues**标签，任务发布与技术问题讨论就是在这里，有点类似BBS（当然没那么水），据 全职陪练-CnFeat说，Issues还可以用来[写blog](https://github.com/lifesinger/lifesinger.github.io/issues)，各种意想不到。**PullRequest**标签，可以将自己fork后修改的内容申请合并到原仓库中，不过大妈说，本仓库作为所有学员的模板仓库，不接受PR。**wiki**标签，[官方介绍](https://help.github.com/articles/about-github-wikis/)说可以用来写任何东西，如技术文档，本仓库wiki主要是各种各种规约和岩钉。**Pulse**和**Graphs**标签，貌似是一些数据统计，待需要时详查。
## gitbook配置
* 打开[gitbook](https://www.gitbook.com)，选择用GitHub账号登陆
* Create a new book，选择从GitHub，选择仓库（就是从开智OMOOC2py fork的仓库），输入标题，更改链接（可选），点Create Book, gitbook 随即生成
## 使用
git clone后本地修改，git push到GitHub，修改内容会自动同步到Gitbook。

目前尚未碰到群里大家遇到的各种坑，也并未安装gitbook命令行。但在测试的时候，本地修改→git push→gitbook看效果，重复了几次，发现安装gitbook可以直接本地预览，不用
## gitbook-cli安装
```cli
sudo npm install gitbook-cli -g # Need sudo
gitbook init #
gitbook install # intall necessary plugin, like DISQUS
gitbook serve # Not server
```


