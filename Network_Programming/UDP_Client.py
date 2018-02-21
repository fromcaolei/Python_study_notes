#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------UDP_Client------------------------------------\033[0m')
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.sendto(data, ('127.0.0.1', 9999))  #发送数据，不需要调用connect(),直接通过sendto()发送
    print(s.recv(1024).decode('utf-8'))  #接收数据，仍用recv()方法
s.close()