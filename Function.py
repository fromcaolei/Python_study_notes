#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------调用函数----------------------------------------------------\033[0m')
#一些内置函数：
print(abs(-20))  #取绝对值函数
print(max(1, 2, 3, -5))  #返回最大值函数
print(int('123'), int(12.34), bool(1))  #数据类型转换

#指向函数的变量，有点像C中的指向函数的指针：
a = abs  #这里写函数名，因为函数名是指向函数对象的引用
print(a(-22))  #调用a和调用abs一样



print('\n\n\033[0;31;40m-2--------定义函数----------------------------------------------------\033[0m')
#使用def语句定义函数    def 函数名(参数表):
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-22))  #调用方式还可以是在Python交互环境中，使用from 文件名 import 函数名    可以将这个函数载入终端环境，然后执行调用，会在当前路径下生成一个__pycache__

#定义空函数，使用pass语句执行空操作，pass可以在判断语句中做占位符
def nop():
    pass

nop()

#参数检查，在自定义的函数中，可以使用isinstance(变量, (类型1, 类型2...))检查形参类型
if not isinstance(1, (int, float)):  #将1改为一个字符串时会报错
    raise TypeError('bad operand type')

#返回多个值，实际返回的是一个tuple
import math  #表示导入math包，类似C中的include<math.h>

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(1, 2, 1)  #实际返回的是一个tuple，tuple可以给多个变量同时依次赋值
z = move(1, 2, 1)  #此时，z就是一个tuple
print(move(1, 2, 1))  #注意，结果是带括号的，印证了返回结果是一个tuple的说法



print('\n\n\033[0;31;40m-3--------函数的参数--------------------------------------------------\033[0m')
#位置参数（求x的n次方）
def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power1(2, 2))


#默认参数（求x的n次方，默认求平方，不同于C++中的重载函数）
def power2(x, n = 2):  #注意：默认参数必须指向不变对象，不能指向list类型，不然每次调用的结果都不一样
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power2(2))


#可变参数，用*定义（可以用来传入0个或任意个参数，相当于传数组，这些参数默认合并为一个tuple）
def calc(*numbers):  #计算a² + b² + c² + ……
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
nums = [1, 2, 3]
print(calc(*nums))  #若已有一个list或tuple，可在前加一个*简化调用


#关键字参数，用**定义（可以用来传入0个或任意个含参数名的参数，相当于传dict字典的成员，这些参数默认合并为一个dict）
def person1(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person1('Michael', 30)
person1('Michael', 30, city = 'Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person1('Jack', 24, **extra)  #若已有一个dict，可在前加一个**简化调用（传拷贝，非传引用）


#命名关键字参数，用*,调用（用于传入指定dict字典的成员，若参数表中有一个可变参数，后边的命名关键字参数就不需要*,了）
def person2(name, age, *, city, job):  #*,之后的city和job参数名参数必须传入
    print(name, age, city, job)

person2('jack', 24, city = 'Beijing', job = 'Engineer')


#参数组合，参数定义的顺序必须时：必选参数、默认参数、可变参数、命名关键字参数、关键字参数
#一种特殊用法：
def f1(a, b, c=0, *args, **x):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', x)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)  #通过一个tuple和dict实现调用

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的



print('\n\n\033[0;31;40m-4--------递归函数----------------------------------------------------\033[0m')
#在函数内部调用自身为递归函数，若函数只调用自身，return语句中不含表达式，则称之为尾递归函数，Python未做尾递归优化，所以一样
def fact1(n):  #使用递归函数计算n!=1x2x3x...xn
    if n == 1:
        return 1
    return n * fact1(n - 1)  #含乘法表达式，不是尾递归
print(fact1(10))

def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)  #属于尾递归，使用fact2(1000)还是栈溢出
print(fact2(5))


