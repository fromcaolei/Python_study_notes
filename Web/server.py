#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------Python的内置WSGI服务器------------------------\033[0m')
#Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

from wsgiref.simple_server import make_server
from hello import application_1, application_2  #导入自己编写的application函数

httpd = make_server('', 8000, application_2)  #创建一个服务器，IP地址为空，端口是8000，处理函数是application
print('Serving HTTP on port 8000...')

httpd.serve_forever()  #开始监听HTTP请求

