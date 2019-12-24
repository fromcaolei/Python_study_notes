#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-3--------多线程---------------------------------------\033[0m')
#多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。可以通过多进程实现多核任务。
#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)  #current_thread()函数返回当前线程的实例
t1 = threading.Thread(target=loop, name='LoopThread1')  #使用threading.Thread()函数创建新线程，用LoopThread命名子线程
t2 = threading.Thread(target=loop, name='LoopThread2')  #使用threading.Thread()函数创建新线程，用LoopThread命名子线程
t1.start()
t2.start()
t1.join()  #若不使用join()函数，则两个线程一起执行
t2.join()
print('thread %s ended.\n' % threading.current_thread().name)


#使用锁，好处:确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处:包含锁的某段代码实际上只能以单线程模式执行，效率下降。
#其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
import time, threading
balance = 0
lock = threading.Lock()  #注意这个锁定义的位置一定要是全局变量，需要两个线程都用同一把锁，否则各用各的锁还是会造成结果不为0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        #(1)未使用lock锁的change_it()函数
        #change_it(n)

        #(2)使用lock锁的change_it()函数不会将结果算错。
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
#由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



print('\n\n\033[0;31;40m-4--------ThreadLocal--------------------------------\033[0m')
#若需要为多个子线程传递多层形参时，传递起来较为麻烦，可以使用threading.local()函数定义一个ThreadLocal对象
import threading

local_school = threading.local()  #创建全局ThreadLocal对象

def process_student():
    std = local_school.student  #获取当前线程关联的student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name  #绑定ThreadLocal的student
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()



print('\n\n\033[0;31;40m-5--------进程vs线程-----------------------------------\033[0m')
#计算密集型任务同时进行的数量应当等于CPU的核心数(如计算圆周率、对视频进行高清解码等)
#IO密集型任务，任务越多，CPU效率越高，但也有一个限度(如Web应用、网络、磁盘IO的任务等)



print('\n\n\033[0;31;40m-5--------分布式进程-----------------------------------\033[0m')
#Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上
#通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了

#例子:task_master.py和task_worker.py文件