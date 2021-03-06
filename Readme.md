Python学前了解
==============

Python解释器
------------
* CPython：官方
* IPython：基于CPython的交互式解释器
* PyPy：动态编译，执行速度高
* Jython：运行在Java平台
* IronPython：运行在.NET平台

Python基础
----------

* Python以``缩进``方式编写代码（约定俗成4个空格缩进）
* 以``#``开头的为注释
* 以``:``结尾时缩进的语句视为代码块

第一个Python程序
---------------

在Python交互终端下执行命令：
```shell
>>> 100+200
>>> print('hello, world')  #没有;号
```

在命令行终端下执行Python脚本：
```shell
C:\work>python calc.py
```

Linux和Mac中需要在.py文件中第一行加入：
```python
#!/usr/bin/env python3 
```

python代码中第二行加入：
```python
# -*- coding: utf-8 -*-
```
告诉Python解释器按照UTF-8编码读取源码，以便中文输出不会出错

输入和输出
----------

* print()函数：

```python
print('The quick brown fox', 'jumps over', 'the lazy dog')  #打印字符串
print(300)  #打印整数
print('100 + 200 =', 100 + 200)  #字符串加整数
```

* input()函数：

```python
name = input()  #输入字符串
name = input('please enter your name: ')  #可以设置输入提示
```

数据类型和变量
-------------

整数、字符串、布尔值(注意首字母大写)等数据类型和C++类似。

和其他语言不同的

* ``浮点数``：对于很大或很小的浮点数，就必须用科学计数法表示， 0.000012可以写成1.2e-5
* ``多行内容``：Python允许用'''...'''的格式表示多行内容，用\n写在一行里不好阅读
* ``空值``：None表示，不能理解为0
* ``变量``：同一个变量可以反复赋值，而且可以是不用类型的变量，这是动态语言的特性
* ``常量``：如PI，用全大写的方式表示常量只是一个习惯上的用法，但仍可以改变常量的值
* ``除法``：/计算结果为浮点数，//计算结果为只保留整数

字符串和编码
-----------

* ``ASCII编码``只有127个字符
* ``GB2312编码``为中国制定，用来把中文编进去
* ``Unicode编码``把所有语言都统一到一套编码里
* ``UTF-8编码``把一个Unicode字符根据不同的数字大小编码成1-6个字节，以节省空间

计算机内存中使用Unicode编码，存储在硬盘时转换为UTF-8编码。

编码相关的转换函数
-----------------

* ``ord()函数``：获取字符的整数表示，如ord(“中”)  #得20013
* ``chr()函数``：把编码转换为对应的字符，如chr(25991)  #得“文”
* 以``\u+16进制数``可直接获得对应编码的字符串

Python对bytes类型的数据用带b前缀的单引号或双引号表示： x = b'ABC'

* ``encode()函数``：以Unicode表示的字符串可以使用该函数转换为指定的字节类型。如：

```shell
>>> 'ABC'.encode('ascii')  #纯英文可以编码为字节类型
b'ABC'
>>> '中文'.encode('utf-8')  #中文可以用utf-8编码为字节类型
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')  #会报错，并不在编码范围内
```

* ``decode()函数``：从网络、磁盘上读取的字节流，转变为字符串。如：

```shell
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

* ``len()函数``：计算字符数。如：len('中文'.encode('utf-8'))得到6


输出格式化
----------


```shell
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
```

使用``%``实现格式化，和C语言类似。补3个0使用%03d，补2个空格使用%2d，小数保留2位%.2f，使用%s会把任何数据转换成字符串，使用%%会打印%本身。


关于Python虚拟化环境virtualenv
-----------------------------

用于多个Python应用程序独立运行于不同的系统环境时使用（如：jinja2.7、jinja2.6）
先安装这个虚拟化工具：

```shell
pip3 install virtualenv
```

然后在所需目录下创建一个独立的Python运行环境

```shell
virtualenv --no-site-packages [environ_name]
```

进入该环境，即可在该环境下独立配置所需版本的模块或环境：

```shell
source [environ_name]/bin/activate
```

退出该环境：

```shell
deactivate
```

单步方式运行
-----------------------------

启动Python的调试器``pdb``，让程序以单步方式运行，可以随时查看运行状态：

```shell
python -m pdb test.py
```

在程序中设置断点：

```python
import pdb  #先导入pdb环境
pdb.set_trace()  #可能出错的地方放置本行，运行到这里会自动暂停，进入调试环境
```

在调试环境中，使用``n``单步执行代码，使用``l``查看当前运行代码，使用``p [变量名]``查看变量当前值，使用``c``继续运行，使用``q``退出调试环境，结束程序。