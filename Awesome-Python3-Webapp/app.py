#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):  #参数request包含了所有浏览器发过来的HTTP协议里的信息，参考http://aiohttp.readthedocs.org/en/stable/web_reference.html
    return web.Response(content_type='text/html', body=b'<h1>Awesome</h1>')  #注意，源代码中没有content_type='text/html'，会变成下载一个HTML文件而不是访问。该函数参数列表：class aiohttp.web.Response(*, status=200, headers=None, content_type=None, body=None, text=None)

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)  #创建web服务器，用于处理URL和HTTP协议
    app.router.add_route('GET', '/', index)  #将处理函数注册到指定的访问路径，用于响应"GET"请求
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)  #用协程创建监听服务，loop为传入函数的协程。返回的srv为一个创建好的，绑定ip、端口、HTTP协议簇的监听服务协程，srv的行为模式和loop.create_server()一致
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()  #创建协程
loop.run_until_complete(init(loop))  #运行协程，直到完成
loop.run_forever()  #运行协程，直到调用stop()