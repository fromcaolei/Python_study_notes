#!/usr/bin/env python3
## -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------文件读写------------------------------------\033[0m')
#Python内置了读写文件的函数，用法和C是兼容的。
try:
    f = open('./uptime.sh', 'r')
    print(f.read(80))  #若read()无参数则会打印全部内容，若文件较大则不安全
    print("\n")
finally:
    if f:
        f.close()  #一定要关闭，这点和C/C++/C#一样

#读取二进制、十六进制文件可用rb选项，encoding参数读取非UTF-8编码的文件使用，如gbk；errors参数可设置忽略编码不规范的文件错误
#with open('./uptime.sh', 'r', encoding='gbk', errors='ignore') as f:
with open('./uptime.sh', 'r') as f:  #使用with...as的方式防止忘记close，和C#中的using(){}意义一样
    print(f.readline())  #打印一行
    lists = f.readlines()  #readlines()方法返回一个list
    print(lists)
    for s in lists:
        print(s.strip())  #strip()方法会把行末的\n删除

#写文件，调用open()时，使用w、a、wb、ab选项，w是写，a是追加，b是二进制文件
with open('./uptime.sh', 'a') as f:
    #f.write('#hello,world\n')
    pass
    



print('\n\n\033[0;31;40m-2--------StringIO和BytesIO--------------------------\033[0m')
#StringIO就是在内存中读写str，首先创建一个StringIO对象，然后向读写文件一样的操作
from io import StringIO

#IDE奇怪的报错，在终端下直接执行不报错，未解决
with StringIO('Hello!\nHi!\nGoodbye!') as strio:
    while True:
        ss = strio.readline()
        if ss == '':
            break
        print(ss.strip())  #strip()方法会把行末的\n删除

#使用write()方法
strio = StringIO()
strio.write('hello')
strio.write(' ')
strio.write('world!')
print(strio.getvalue())  #getvalue()方法用于获得写入后的str
strio.close()


#BytesIO和StringIO类有一致的接口，用于读写内存中的二进制数据
from io import BytesIO
with BytesIO(b'\xe4\xb8\xad\xe6\x96\x87') as f:
    print(f.read())
    f.write('中文'.encode('utf-8'))
    print(f.read())  #这里打印为空就搞不明白了
    print(f.getvalue())

