#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------高阶函数-------------------------------------------\033[0m')
#可以改变模块中默认函数变量的指向，如：abs = 10，这时候就无法使用abs(-10)计算绝对值了,要使abs变量的指向在其他模块中生效，使用：import builtins; builtins.abs = 10
#函数名也可以当做变量传给另一个函数作为形参



print('\n\n\033[0;31;40m-2--------map------------------------------------------------\033[0m')
#map()函数第一个参数使用函数对象，第二个参数使用一个可迭代对象，会把每个元素依次作用到函数上返回新的 迭代器。
#就像C++去迭代一个函数对象一样：for_each(iterator.begin(), iterator.end(), 函数对象)

print(list(map(str, [1, 2, 3, 4, 5, 6, 7])))  #将数字转为字符串，不使用list函数无法显示迭代器中的所有内容



print('\n\n\033[0;31;40m-3------------reduce-----------------------------------------\033[0m')
#reduce()函数第一个参数使用二元函数对象，第二个参数使用一个可迭代对象，实现把结果和序列的下一个元素再带入函数对象，返回一个 可迭代对象
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 2, 3, 4, 5]))  #做1-5的累加
print(sum([1, 2, 3, 4, 5]))

def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 2, 3, 4, 5]))  #将序列变为整数



print('\n\n\033[0;31;40m-4--------filter----------------------------------------------\033[0m')
#filter()函数用来过滤可迭代对象中不需要的值。接收一个函数和一个可迭代对象，然后把函数对象返回值为true的值保留，返回一个 迭代器
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5])))



print('\n\n\033[0;31;40m-5--------sorted----------------------------------------------\033[0m')
#sorted()函数用来为可迭代对象进行排序，第一个参数使用一个可迭代对象，第二个参数为命名关键字参数key传入函数对象(abs、str.lower)，第三个参数为命名关键字参数reverse传入bool值用来改变顺逆序，返回一个 可迭代对象

list1 = [36, 5, -12, 9, -21]
print(sorted(list1))
print(sorted(list1, key = abs))
print(sorted(list1, key = abs, reverse = True))

list2 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(list2))
print(sorted(list2, key = str.lower))
print(sorted(list2, key = str.lower, reverse = True))



print('\n\n\033[0;31;40m-6--------返回函数--------------------------------------------\033[0m')
#使用函数作为返回值，在一个函数内部定义另一个函数，然后大函数返回里面定义的函数对象。这种程序结构成“闭包”，调用这个大函数返回值时，需要带上括号。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:  #注意返回闭包时，不要使用大函数中的任何循环变量，否则容易失误总是调用到该变量的最后一个值
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())



print('\n\n\033[0;31;40m-7--------匿名函数--------------------------------------------\033[0m')
#lambda即匿名函数，函数只能有一个表达式，不用写return，返回该表达式的结果。
l = lambda x: x * x
print(l(4))

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))



print('\n\n\033[0;31;40m-8--------装饰器----------------------------------------------\033[0m')
#要增强函数的功能，又不希望修改函数的定义，这种在代码运行期间动态增加功能的方式成为“装饰器”decorator。本质上是返回函数的高阶函数。
import functools
def log(func):
    @functools.wraps(func)  #添加此行可以不修改传入函数的__name__参数
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log  #一种使用decorator的语法，使用@将decorator置于函数的定义处
def now():
    print('2018-1-14')

now()  #调用函数时，会先执行decorator,等同于now = log(now)
print(now.__name__)  #会修改now()函数的__name__参数



print('\n\n\033[0;31;40m-8--------偏函数----------------------------------------------\033[0m')
#自定义一个函数对象，将另一个函数的参数或命名关键字参数绑定默认值后，传入自定义的函数中，方便二次掉用形参一样的情况。
print(int('7B', base = 16))  #base默认值为10,16代表以16进制数解码'7B'

import functools
int16 = functools.partial(int, base = 16)
print(int16('7B'))  #偏函数会讲int函数的参数值绑定后，赋予函数对象int16

#偏函数还可以默认传入位置型参数
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))  #等同于调用max(10, 5, 6, 7)
int2 = functools.partial(int, '20')
print(int2())  #会打印20
