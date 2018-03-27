#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------协程--------------------------------\033[0m')
#协程在执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行，类似单片机中的触发中断。
#实际上是一种yield关键字的高级用法，代码每次遇到yield就返回，如同return，但当再次next()调用或迭代，就从这里继续执行，yield也能通过其他函数调用这个生成器(包含yield的函数就是生成器)的send()函数给这个生成器发送数据，并同时继续执行一次生成器。
#和多线程相比，优势就是协程极高的执行效率，不需要多线程的锁机制

def consumer():
    r = ''
    while True:
        n = yield r  #另一个函数发送的值会赋给n
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
        
def produce(c):
    c.send(None)  #第一次需要发送一个空值，使生成器先跑起来，否则不存在断点，无法继续
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  #不再使用生成器时将其关闭

c = consumer()
produce(c)