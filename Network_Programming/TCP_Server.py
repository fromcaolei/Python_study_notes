#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------TCP_Server------------------------------------\033[0m')
#1、首先要绑定一个端口用来监听其他客户端的连接
#2、服务器与客户端建立socket连接，随后的通信就靠这个Socket连接了

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建一个基于IPv4和TCP协议的Socket
s.bind(('127.0.0.1', 9999))  #服务器将IP地址绑定到某一块网卡的地址上，也可以是0.0.0.0，绑定到127.0.0.1时，客户端必须同时在本机运行才能连接
s.listen(5)  #listen()方法开始监听端口，设置等待连接的最大数量
print('Waiting for connection...')

def tcplink(sock, addr):  #发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':  #注意：当客户端进程停止，或客户端close掉socket时，连接会断开，导致循环退出，data会变为b''，not data会置为true
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock, addr = s.accept()  #接受一个新连接，等待并返回一个客户端的连接，addr是一个包含IP地址和端口的tuple，sock是一个客户端的socket对象
    t = threading.Thread(target=tcplink, args=(sock, addr))  #不断创建新线程来处理TCP连接，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
    t.start()