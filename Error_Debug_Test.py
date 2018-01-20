#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------错误、调试、测试----------------------------------\033[0m')
print('\n\n\033[0;31;40m-2--------错误处理-----------------------------------------\033[0m')
#Python的try...except...finally...机制，和C#类似，但多了可以使用else来在没有错误时执行
try:
    print('try...')
    r = 10 / 0
    print('result: %s' % r)
except ZeroDivisionError as e:  #若未知错误类型需要获得异常，可调用BaseException或Exception
    print('except:', e)
else:
    print('not error...')
finally:
    print('finally...')
print('END...\n')

#使用raise关键字抛出自定义异常，但尽量使用Python内置的错误类型。一般抛出异常的代码如下：
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)  #这是个系统内置类型的异常，可以直接调用
    return 10 / n

def bar():
    try:
        foo('1')  #这里改成'0'看结果
    except ValueError as e:
        print('ValueError!')
        raise  #这里并不多余，raise后若不带参数，会抛出解释器所抛出的异常,但会打断程序执行

bar()

print('\n\n\033[0;31;40m-3--------调试---------------------------------------------\033[0m')
