#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------socket_sina------------------------------------\033[0m')
#socket用于打开一个网络连接，需要为其指定目标地址类型、通信协议、目标地址、端口号，进行建立连接
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET表示使用IPV4协议，SOCK_STREAM表示面向流的TCP协议
s.connect(('www.sina.com.cn', 80))  #建立连接，参数为tuple
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')  #发送请求，要求返回首页内容(发送的文本格式必须符合HTTP标准)

buffer = []
while True:
    d = s.recv(1024)  #接收数据，设定一次最多接收指定的字节数
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)  #将http头和网页分离
print(header.decode('utf-8'))  #打印HTTP头
with open('sina.html', 'wb') as f:  #把网页内容写入文件
    f.write(html)  #只需要在浏览器中打开这个sina.html文件，就可以看到新浪的首页了