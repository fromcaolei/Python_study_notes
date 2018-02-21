#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------socket_sina------------------------------------\033[0m')
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))  #建立连接，类似连接新浪网站，但发送的请求可以是自定义的
print(s.recv(1024).decode('utf-8'))  #接收欢迎消息
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)  #发送请求
    print(s.recv(1024).decode('utf-8'))  #接收数据
s.send(b'exit')
s.close()