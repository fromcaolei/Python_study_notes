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
