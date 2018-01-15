#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------面向对象编程-------------------------------------\033[0m')
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print(bart.name)



print('\n\n\033[0;31;40m-2--------类和实例-----------------------------------------\033[0m')
#1、类通过class关键字定义，接着是类名(首字母大写)，接着是(object)表示类的继承关系，通常为object；
#2、构造函数为__init__方法，第一个参数永远是self，代表创建的实例本身，可以使用self在构造函数中绑定各种属性；
#3、类中定义的函数第一个参数永远是self，self本身就拥有构造时定义的所有数据；
#4、创建类的实例使用'变量 = 类名()'实现，括号中传递构造函数形参，不需要传递self参数；



print('\n\n\033[0;31;40m-3--------访问限制-----------------------------------------\033[0m')
