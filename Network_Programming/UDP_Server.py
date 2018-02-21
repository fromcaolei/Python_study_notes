#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------UDP_Client------------------------------------\033[0m')
#面向无连接的的协议，比TCP快
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #SOCK_DGRAM表示为UDP
s.bind(('127.0.0.1', 9999))  #服务器将IP地址绑定到某一块网卡的地址上，也可以是0.0.0.0，绑定到127.0.0.1时，客户端必须同时在本机运行才能连接
print('Bind UDP on 9999...')

while True:  #注意：省掉了多线程
    data, addr = s.recvfrom(1024)  #接收数据和客户端的地址与端口，addr是一个包含IP地址和端口的tuple，data就是bytes数据了
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)  #给客户端返回数据，注意因为没有客户端发送过来的socket，就需要指定addr参数来指定目的地址
