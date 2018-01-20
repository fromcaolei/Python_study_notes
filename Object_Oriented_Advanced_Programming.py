#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------面向对象高级编程---------------------------------\033[0m')
print('\n\n\033[0;31;40m-2--------使用__slots__------------------------------------\033[0m')
#对于一个对象，可以动态的为其绑定属性或方法，对于类也可以动态绑定方法，但在类的__slots__属性中定义了要绑定的属性后，就只能绑定规定的相关属性,其子类不会继承__slots__属性，但当子类重写该属性时，就会获得父类和自定义内容的并集。C++中的动态绑定是重写虚函数
class Student(object):
    __slots__ = ('name', 'age', 'set_age')  #用tuple定义允许绑定的属性或名称
s = Student()

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  #给一个对象动态绑定方法
s.set_age(25)
print(s.age)

Student.set_age = set_age  #给一个类动态绑定方法，之后定义的对象都会有这个方法



print('\n\n\033[0;31;40m-3-------使用@property-------------------------------------\033[0m')
#通常操作一个类中的属性时，可以在类中写get()、set()之类的方法来返回或赋值操作，但要修改该属性，就需要调用方法去执行。可以使用@property装饰器来时get、set方法像调用属性一样的调用
class Student(object):

    @property  #负责把一个方法当做一个属性来调用
    def score(self):  #注意，两个方法名字相同
        return self._score

    @score.setter  #前面使用过@property，就会自动创建@score.setter修饰器。若两者之一没有写，则该属性就会是一个只读或只写属性
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 20
print(s.score)



print('\n\n\033[0;31;40m-4--------多重继承-----------------------------------------\033[0m')
#通过多重继承，一个子类就可以同时获得多个父类的所有功能，多继承称之为mixIn



print('\n\n\033[0;31;40m-5--------定制类-------------------------------------------\033[0m')
#Python中有很多特殊用途函数，可以帮助我们定制类
#__str__()   直接使用print打印一个对象时，会调用该方法，若未写则报错

#__repr__()   不使用print打印，直接调用对象时，会调用该方法，通常和__str__()方法内容一样

#__iter__()   支持类被迭代，该方法返回一个迭代对象，然后会不停的执行__next__()方法取值
class Fib(object):  #该类可直接被迭代 for n in Fib():
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

#__getitem__()   使可迭代的类实现使用角标、切片slice
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print('\n', f[5])

#__getattr__()   对调用到不存在的属性或函数时，会调用该函数
class Chain(object):  #一种链式调用，实现方便调用API

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

#__call__()   想让一个对象如同使用函数一样用括号执行，会调用该函数，类似C++的括号运算符重载，即函数对象
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s() # self参数不要传入



print('\n\n\033[0;31;40m-6--------使用枚举类---------------------------------------\033[0m')
#一种简单的枚举设计方法：
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#较为严谨的设计方法：
from enum import Enum, unique

@unique  #@unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6



print('\n\n\033[0;31;40m-7--------使用元类-----------------------------------------\033[0m')
#动态与静态语言最大的不同是函数了类的定义，是在运行时动态创建的，而不是编译时定义的
#type()函数，可以查看一个变量的类型，可以以用来创建类。实际上Python在运行时，仅仅是扫描一下class定义的语法，然后调用type()函数创建类
def fn(self, name = 'world'):  #先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello = fn))  #创建Hello类
h = Hello()
h.hello()

#metaclass为元类，目前无法掌握，也基本不会用到
