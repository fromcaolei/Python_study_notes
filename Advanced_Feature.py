#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------切片-------------------------------------------------\033[0m')
#切片，一种截取list、tuple、字符串等类型的操作符':'，类似C#中Substring()
L = list(range(11))
print(L)
print(L[0:3])  #截取前3个，不包括3的元素，也支持从负值开始即：L[-1:10]得到10
print(L[0:7:2])  #每隔2个截取一个,到第七个元素为止

print((0, 1, 2, 3, 4, 5)[:3])  #对tuple使用,':'前面不谢值等同于0

print('ABCDEFG'[:3])  #对字符串使用



print('\n\n\033[0;31;40m-2--------迭代-------------------------------------------------\033[0m')
#属于for...in循环的使用方式补充
#dict类型：
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)  #默认dict迭代key

for value in d.values():
    print(value)  #迭代value

for k, v in d.items():
    print(k, v)  #迭代整个元素

#字符串类型：
for ch in 'ABC':
    print(ch)

#list类型，将元素和角标一起迭代出来，适用enumerate()函数
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

#判断一个对象是否可被迭代，使用collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc', Iterable))  #可以迭代
print(isinstance(123, Iterable))  #不能迭代



print('\n\n\033[0;31;40m-3--------列表生成式-------------------------------------------\033[0m')
#用来生成一些有规律list的语法，减少for循环的使用

#生成[1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1, 11)])  #把要生成元素的公式写在前方，后面跟for循环即可，注意前面公式中的变量和迭代中的变量要一致

#使用两层for循环
print([m + n for m in 'ABC' for n in 'XYZ'])

#生成当前目录下所有文件
import os
print([d for d in os.listdir('.')])

#使用两个变量生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

#把list中的所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])



print('\n\n\033[0;31;40m-4--------生成器-----------------------------------------------\033[0m')
#这种用法可以使大量数据一边循环生成，一边使用，这种机制称为生成器：generator
#tuple可以使用列表生成式生成一些简单的generator，也可以在函数中使用yield关键字生成复杂的generator
g = (x * x for x in range(10))
print(g)
print(next(g))  #使用next()函数或for循环迭代的方式动态的生成g和使用g内部的内容
print(next(g))
for n in g:
    print(n)  #前面使用两个print调用过g所以这里的print中不会出现generator中的前两个成员


def fib(max):  #斐波那契数列，使用yield关键字生成复杂generator:
    n, a, b = 0, 0, 1
    while n < max:
        yield b  #代码每次遇到yield就返回，如同return，但当再次next()调用或迭代，就从这里继续执行
        a, b = b, a + b  #等同于a = b, b = a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)  #迭代到最后会拿不到'done'的返回值，需要捕获StopIteration错误中的value

g = fib(6)  #不能讲fib(6)卸载while内部，不然会无限创建generator，不同于上边的for循环只创建一次
while True:
    try:
        print(next(g))
    except StopIteration as e:  #捕获StopIteration
        print('Generator return value:', e.value)
        break



print('\n\n\033[0;31;40m-5--------迭代器-----------------------------------------------\033[0m')
#可用for循环迭代的对象称之为可迭代对象iterable
#既可以用for循环迭代的，也可以使用next()函数迭代的对象成为迭代器iterator

from collections import Iterable
from collections import Iterator
print(isinstance([], Iterable))  #查看对象是否为可迭代对象
print(isinstance((x for x in range(10)), Iterator))  #查看对象是否为迭代器

print(isinstance(iter([]),Iterator))  #iter()函数可以讲一个可迭代对象变换为迭代器
