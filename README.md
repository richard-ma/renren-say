renren-say
==========

Renren dot com status robot

人人网状态机器人

安装
----------

1. 下载代码
1. 将config.ini.sample重命名为config.ini
1. 修改config.ini中的email和password修改成人人网账户的邮箱和密码

配置运行模式
----------

修改config.ini中的runtime段里的mode变量值：

* 指定插件模式：插件名（不含Plugin），每次运行将运行指定的插件
* 随机模式：random，每次使用随机算法选出一个插件运行

默认使用随机模式运行，增加趣味性

使用方法
----------

* 命令行下运行renren-say.py
* 也可将此命令使用cron定时运行

插件开发
----------

* 给插件起一个名字，比如xxx
* 在plugins目录下新建一个文件xxxPlugin.py
* 文件内容为一个类，类名和文件名相同
* xxxPlugin类中必须有\_\_init\_\_和say两个方法
* 细节请参考目录中的SimplePlugins.py和YuebaoPlugin.py两个文件

TODO
----------

* 开发更多有意思的插件，欢迎大家提交PR
* 分离随机数产生方法，做到更智能
