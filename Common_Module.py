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
    with open('./uptime.sh', 'rb') as fp: 
        while True:
            blk = fp.read(4096)  #4KB per block
            if not blk: break
            m.update(blk)
    print(m.hexdigest())

main()



print('\n\n\033[0;31;40m-5--------hmac--------------------------------------\033[0m')
#是一种添加私有字符串的哈希加密算法，和hashlib不同的是，hmac传入的key和message都是byte类型
import hmac

message = b'Hello, world!'  #byte类型
key = b'secret'  #byte类型
h = hmac.new(key, message, digestmod='MD5')  #如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())



print('\n\n\033[0;31;40m-5--------itertools---------------------------------\033[0m')
#提供了一些有规律的迭代器或方法，辅助做一些别的事情，在for迭代时才会无限地迭代下去，本生不会事先把元素生成出来，类似惰性数组
#一个生成无限自然数的迭代器count()，count(1)相当于range(+∞)
import itertools

natuals = itertools.count(1)
#for n in natuals:
#    print(n)

#将一个序列无限重复下去，即循环播放cycle()
cs = itertools.cycle('ABC')  #例如字符串序列
#for c in cs:
#    print(c)

#也有把一个元素无限循环播放下去的repeat(）
ns = itertools.repeat('A', 3)  #给定第二个参数可以指定重复次数
for n in ns:
    print(n)

#通过一个方法截取需要的有限部分序列takewhile(）
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)  #这个匿名函数有些类似C++的函数对象
print(list(ns))

#用于串联两个迭代对象的函数chain()
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#用于把相邻且相同的两个元素挑出来groupby()
for key, group in itertools.groupby('AAABBBCCAAA'):  #单纯的讲相同的元素拿出，返回其元素值和重复的list
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):  #可通过匿名函数将不区分大小写
    print(key, list(group))



print('\n\n\033[0;31;40m-6--------contextlib--------------------------------\033[0m')
#其实任何对象，只要实现了上下文管理，就可以用with语句，实际代码不一定用于调用类似open()函数的close()函数
#普通用法，with开始时，调用__enter__()方法，结束时调用__exit__()方法：
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

#可以使用一种装饰器contextmanager配合yield简化上述方法（虽然我觉的根本没简化，反倒难以理解了）
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q  #用yield来隔离上下文的内容
    print('End')

with create_query('Bob') as q:  #这样做的用处是，在某段代码执行前后自动执行特定代码，普通的装饰器只在代码执行前执行
    q.query()

#下面代码自动给一段字符串添加xml节点
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("\thello")
    print("\tworld")

#对于没有实现上下文的对象，用closing()来把该对象变为上下文对象，closing也是一个经过@contextmanager装饰的generator
from contextlib import closing
from urllib.request import urlopen

#with closing(urlopen('https://www.python.org')) as page:
#    for line in page:  #打印这个网页的HTML语句
#        print(line)



print('\n\n\033[0;31;40m-7--------urllib------------------------------------\033[0m')
#urllib提供了一系列用于操作URL的功能，先了解：GET-从指定的资源请求数据。POST-向指定的资源提交要被处理的数据。HEAD-与GET相同，但只返回 HTTP 报头，不返回文档主体。
'''
from urllib import request

#发送一个GET请求到指定的页面，然后返回HTTP的响应
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))  #k是参数名，v是值
    print('Data:', f.read().decode('utf-8'))  #HTTP响应的头和JSON数据


#模拟浏览器发送GET请求，模拟iPhone 6，通过往Request对象添加HTTP头
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')  #往Request对象添加HTTP头
with request.urlopen(req) as f:  #在这再使用urlopen()方法即可返回适配iPhone6的json数据
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

#以POST发送一个请求，把参数data以bytes形式传入
#未学习

#通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
#proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
#proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
#proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
#opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
#with opener.open('http://www.example.com/login.html') as f:
#    pass



print('\n\n\033[0;31;40m-8--------xml---------------------------------------\033[0m')
#解析XML，在Python中使用SAX（流模式），自己写三个事件start_element、char_data、end_element来解析XML中的开标记、内容、闭标记
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
#parser.Parse(xml)  #这段代码有问题，尚不知问题所在

#拼接字符串的方法生成XML
L = []
L.append(r'<?xml version="1.0"?>')  #加r前缀，就不用考虑转义的问题，类似C#中的@前缀
L.append(r'<root>')
L.append('some & data')  #好像不支持字节类型
L.append(r'</root>')
print(''.join(L))


print('\n\n\033[0;31;40m-9--------HTMLParser-----------------------------------\033[0m')
#解析HTML，HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML，Python提供了HTMLParser来非常方便地解析HTML
#特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):  #可以获得元素开标记
        print('<%s>' % tag)

    def handle_endtag(self, tag):  #可获得元素闭标记
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):  #每个标记间的内容
        print(data)

    def handle_comment(self, data):  #获得注释内容
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')  #可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去