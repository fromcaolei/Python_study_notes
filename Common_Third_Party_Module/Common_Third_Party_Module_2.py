#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-4--------chardet----------------------------------\033[0m')
#用来检测一条字符串的编码格式
import chardet

print(chardet.detect(b'Hello, world!'))  #会以JSON的形式打印出编码类型、概率、和语言

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))



print('\n\n\033[0;31;40m-5--------psutil------------------------------------\033[0m')
#用来调用系统信息，比subprocess进程模块方便
import psutil  
'''
若提示:No module named 'psutil'
且：pip install psutil无效
则尝试：sudo apt-get install python3-pip
再执行：pip3 install psutil
'''

print(psutil.cpu_count())  #CPU逻辑数量
print(psutil.cpu_count(logical=False))  #CPU物理核心
print(psutil.cpu_times())  #统计cpu的用户、系统、空闲时间

print(psutil.virtual_memory())  #获取内存信息
print(psutil.swap_memory())  #获取swap信息

print(psutil.disk_partitions())  #获取磁盘分区信息
print(psutil.disk_usage('/'))  #获取磁盘使用情况
print(psutil.disk_io_counters())  #获取磁盘IO

print(psutil.net_io_counters())  #获取网络读写字节／包的个数
print(psutil.net_if_addrs())  #获取网络接口信息
print(psutil.net_if_stats())  #获取网络接口状态
#print(psutil.net_connections())  #获取当前网络连接信息，需要root权限

#p = psutil.Process(3776)  #获取指定进程ID=3776，其实就是当前Python交互环境
#print(p.name())  #进程名称

for x in range(10):  #CPU使用率，每秒刷新一次，累计10次
    print(psutil.cpu_percent(interval=1, percpu=True))

print(psutil.test())  #test()函数，可以模拟出ps命令的效果