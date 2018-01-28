#!/usr/bin/env python3
## -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------进程和线程------------------------------------\033[0m')
print('\n\n\033[0;31;40m-2--------多进程---------------------------------------\033[0m')
#实现多线程的方式多种多样，在Linux下可以使用fork()函数或封装了fork()函数的相关多线程类来实现多线程
#一些辅助函数：os.getpid():当前进程调用会返回其进程的ID；os.getppid()子进程调用返回父进程的ID，父进程调用返回0；
#1、直接使用fork()函数，使用其返回值得知是否为子进程或主进程
'''
import os

print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''

#2、使用进程池，一次创建多个进程，运行此例子时，将上边例子注释，否则上边创建的两个进程会将下方代码执行两次,尚不清楚如何停止一个进程

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


#3、子进程，用于调用一个外部进程(例如一条命令)，需要控制子进程的输入和输出
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')  #相当于在命令行执行命令nslookup，然后手动输入：set q=mx python.org exit
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#4、进程间通信，Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去
from multiprocessing import Process, Queue
import os, time, random

def write(q):  #写数据进程执行的代码:
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):  # 读数据进程执行的代码:
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

#5、由于Windows没有fork调用，使用multiprocessing跨平台版本的多进程模块
from multiprocessing import Process
import os

def run_proc(name):  #子进程要执行的代码
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()  #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')

print('\n\n\033[0;31;40m-3--------多线程---------------------------------------\033[0m')
#