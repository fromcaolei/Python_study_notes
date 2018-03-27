#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------asyncio--------------------------------\033[0m')
#如果在函数使用了coroutine装饰器，就可以通过yield from去调用async def声明的函数，如果已经使用async def声明，就没有必要再使用装饰器了，这两个功能是一样的。

import asyncio
import threading

'''
@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(5)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
'''



@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(2)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]  #将需要异步的函数作为一个list传入异步处理函数中
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


'''
#异步网络连接来获取sina、sohu和163的网站首页
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))  #一个模块中两个run_until_complete一起用会报错
loop.close()
'''


print('\n\n\033[0;31;40m-2--------async/await--------------------------------\033[0m')
#把@asyncio.coroutine替换为async；把yield from替换为await。

@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")

#等价于：
async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")