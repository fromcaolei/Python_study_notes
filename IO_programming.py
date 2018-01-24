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



print('\n\n\033[0;31;40m-3--------操作文件和目录-------------------------------\033[0m')
#Python内置的os模块可以直接调用操作系统提供的接口函数，复制文件的函数不在os中，在shutil模块中，使用copyfile()函数
import os
print(os.name)  #查看操作系统类型，'posix'为Linux、mac，'nt'为Windows
print(os.uname())  #获取系统详细信息
#print(os.environ)  #获取操作系统的环境变量
print(os.environ.get('PATH'))  #获取某一个环境变量
print(os.path.abspath('.'))  #查看当前目录绝对路径
os.mkdir(os.path.join('./', 'testdir'))  #创建一个目录，注意尽量使用path.join方法，这样拼接的路径会自动适应当前操作系统的路径分隔符
os.rmdir(os.path.join('./', 'testdir'))  #删掉一个目录
print(os.path.split('/Users/michael/testdir/file.txt'))  #拆分路径，将路径和文件名(或最后一级目录)分离
print(os.path.splitext('/path/to/file.txt'))  #拆分扩展名
#os.rename('text.txt', 'text.py')  #修改文件名
#os.remove('text.py')  #删除文件
print([x for x in os.listdir('.') if os.path.isdir(x)])  #过滤文件，列出当前目录中的所有目录，返回list
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])  #过滤文件，列出当前目录中的所有.py文件，返回list



print('\n\n\033[0;31;40m-4--------序列化---------------------------------------\033[0m')
#类似C#的串行化对象，将代码中的数据或对象化为一种特定编码存于硬盘上

#Python的序列化，叫做pickling，使用pickle模块实现序列化
import pickle
d = dict(name='Bob', age=20, score=88)

print(pickle.dumps(d))  #dumps()将一个对象序列化为一个bytes

with open('./dump.txt', 'wb') as f:
    pickle.dump(d, f)  #dump()函数将d对象写入文件dump.txt中

with open('./dump.txt', 'rb') as f:
    print(pickle.load(f))  #load()函数将dump.txt文件中的序列化内容反序列化

#将对象序列化为标准格式的JSON对象，使用json模块实现
import json

dd = json.dumps(d)  #dumps()将一个对象序列化为JSON的str
print(dd)

print(json.loads(dd))  #loads()函数将JSON反序列化为Python

#将class的实例序列化为JSON对象，需要自行写出关于序列化为JSON的函数，JSON同样可以使用file-like-object的方式
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {'name': std.name, 'age': std.age, 'score': std.score}

s = Student('Bob', 20, 88)
ss = json.dumps(s, default=student2dict)  #使用dumps()的第二个命名关键字参数default传入这个支持将Student类序列化为JSON的函数
print(ss, 'ss')
print(json.dumps(s, default=lambda obj: obj.__dict__))  #提别的：使用匿名函数调用这个类中自有的__dict__属性(该属性默认将对象转换为一个dict)进行序列化

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(ss, object_hook=dict2student))  #使用loads()的第二个命名关键字参数object_hook传入这个支持将JSON反序列化为class对象的函数



os.remove(os.path.join('./', 'dump.txt'))  #注释掉该行可看到被序列化的对象写入的文件