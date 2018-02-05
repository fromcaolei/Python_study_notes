#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------常用內建模块------------------------------\033[0m')
print('\n\n\033[0;31;40m-2--------datetime--------------------------------\033[0m')
#datetime，处理日期和时间的标准库
from datetime import datetime
now = datetime.now()
print(now)  #获取当前的datetime
print(datetime(2015, 4, 19, 12, 20))  #用指定日期创建datetime

print(now.timestamp())  #把datetime转换为timestamp，即从1970/1/1开始计算的时间
print( datetime.fromtimestamp( now.timestamp() ) )  #把timestamp转换为datetime
print(datetime.utcfromtimestamp(now.timestamp()))  #UTC时间，把timestamp转换为UTC时间

print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))  #把字符串转换为datetime
print(now.strftime('%a, %b %d %H:%M'))  #把datetime转换为字符串

from datetime import timedelta
print(now + timedelta(hours=10))  #datetime加减
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))  #创建时区UTC+8:00
print(now.replace(tzinfo=tz_utc_8))  #强行给datetime设置一个时区

#时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  #拿到UTC时间，并强制设置时区为UTC+0:00
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  #astimezone()将转换时区为北京时间
print(bj_dt)



print('\n\n\033[0;31;40m-2--------collections-----------------------------\033[0m')
#Python中的一种高级集合模块

#tuple -> namedtuple  用来创建自定义的tuple对象，如坐标、圆等
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])  #定义名称，定义若干角标(用于引用)
p = Point(1, 2)  #也是tuple类型对象，具备tuple的不变性，又可以根据属性来引用不需要使用角标
print(p.x, p.y)

#list -> deque  list是线性存储，数据量大的时候，插入和删除效率很低，deque方便快速插入和删除
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')  #比list多出的函数
print(q)
q.pop()
q.popleft()  #比list多出的函数
print(q)

#dict -> defaultdict  对比dict，可设定查找不存在的key时，返回自定义的值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
print(dd['key'])  #key2不存在，返回默认值，默认值是匿名函数的返回

#dict -> OrderedDict  对比dict，该类型是有序的，在迭代时不会乱序出现，遵循先入先出的原则
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])  #传统dict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  #OrderedDict
print(d, od)

#Counter是一个简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)  #计算出每个字母出现的次数



print('\n\n\033[0;31;40m-3--------base64-----------------------------------\033[0m')
#是一种用64个字符来表示任意二进制数据的方法。将字符串的原本8bit一字节的方式拆分成6bit一字节的方式，一般一次转换三字节(因为刚好3*8=24=4*6)，将三字节变成四字节，然后将新的内容通过查表获得base64编码
import base64
base = base64.b64encode(b'binary\x00string')  #编码
print(base)
print(base64.b64decode(base))  #解码

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))  #编码结果会出现+/，在URL中不能直接使用
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))  #该方法结果会将+/转换为-_
print(base64.urlsafe_b64decode('abcd--__'))  #与之对应的解码方式

#所有的base64编码都是4的倍数，当base64码的末尾省掉=号时，可根据4的倍数作为条件来补齐=号



print('\n\n\033[0;31;40m-4--------struct-----------------------------------\033[0m')
#用于弥补Python不方便处理字节数据类型的模块，将数据按需要转换为byte格式
import struct
str = struct.pack('>II', 10240099, 10240099)  #'>'表示字节顺序是big-endian(还存在little-endian，也就是微机原理中学的数据在寄存器中的存储形式)，I表示4字节无符号整数(即后面参数的值0 <= number <= 4294967295),H表示2字节无符号整数
print(str)  #结果中：b'\x00\x9c@c'其实为16进制数0x009C4063

print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))  #I表示讲前\xf0\xf0\xf0\xf0，H表示后面的\x80\x80，给予的长度不足时会报错



print('\n\n\033[0;31;40m-5--------hashlib----------------------------------\033[0m')
#提供了常见的摘要算法，如MD5，SHA1等等
import hashlib

md5 = hashlib.md5()  #用于计算md5码值
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
#md5.update('how to use md5 in '.encode('utf-8'))
#md5.update('python hashlib?'.encode('utf-8'))  此两句等同于上一句
print(md5.hexdigest())

sha1 = hashlib.sha1()  #用于计算sha1码值
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


def main():  #计算文件的MD5，经测试和操作系统的md5sum命令计算结果一致
    m = hashlib.md5()
    with open('../uptime.sh', 'rb') as fp: 
        while True:
            blk = fp.read(4096)  #4KB per block
            if not blk: break
            m.update(blk)
    print(m.hexdigest())

main()



print('\n\n\033[0;31;40m-5--------hmac--------------------------------------\033[0m')
#