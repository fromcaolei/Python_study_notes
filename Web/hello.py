#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------WSGI接口-------------------------------\033[0m')
#用于提供底层TCP连接、HTTP请求和响应，将己编写的HTML文本发送出去的一种标准接口。
#它只要求开发者实现一个函数，如下application，其中参数environ一个包含所有HTTP请求信息的dict对象，start_response一个发送HTTP响应的函数。start_response函数第一个参数为HTTP的响应代码，第二个参数为一个以list形式的HTTP Header，每个成员都是一个tuple。application的返回值即为HTTP响应中的body

def application_1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

#可以在地址栏输入用户名作为URL的一部分，将返回Hello, xxx!
def application_2(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')  #HTTP请求的所有输入信息都可以通过environ获得
    return [body.encode('utf-8')]