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
#断言，运行程序时使用-O关闭断言：python -O err.py
n = 1
assert n != 0, 'n is zero!'  #若断言后的判断为false则会打印后面的字符串

#logging，可用一条配置语句控制输出到不同地方
import logging
logging.basicConfig(level=logging.INFO)  #还存在debug，info，warning，error等级别，按级别最高的起作用

s = '1'  #这里改成'0'看结果
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#pdb，单步运行，使用命令:python -m pdb err.py。输入命令l看代码，n下一步，p 变量，q退出，c继续执行

#pdb.set_trace()，在程序中可能出错的地方放入一个pdb.set_trace()需import pdb,就可设置一个断点，在该断点上可操作同上的命令



print('\n\n\033[0;31;40m-4--------单元测试-----------------------------------------\033[0m')
print('\n\n\033[0;31;40m-5--------文档测试-----------------------------------------\033[0m')
#在模块被执行时可运行文档测试，在import引用时，不会自动执行。在代码之后加上：
if __name__=='__main__':
    import doctest
    doctest.testmod()