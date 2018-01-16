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
#1、类中，函数和变量使用'_'、'__'前缀来定义私有private成员，'_'变量可以被访问，但不推荐访问，'__'变量会被Python解释器改成'_类名__变量名'，也可以被访问，但不推荐访问；
#2、可以用'.'来给对象增加一个新变量，如bart.hello = 123 类中不存在hello变量，但也可给其赋值；



print('\n\n\033[0;31;40m-4--------继承和多态---------------------------------------\033[0m')
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):  #继承Animal类，不需要写object类了，因为父类已经继承过了

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

dog = Dog()
print(isinstance(dog, Animal))  #isinstance()函数验证对象类型，该函数的优势时可以判断父类子类关系
print(isinstance(dog, Dog))
print(isinstance(dog, Cat))

#Python是动态语言，对象可以实时修改其类型，在需要调用run方法的地方，不论传入什么样的对象，只要其内部有run方法的定义，就可以被调用，而不会出现调用形参类型错误



print('\n\n\033[0;31;40m-5-------获取对象信息-------------------------------------\033[0m')
#type()函数判断对象类型
import types
print(type(dog))  #在if判断时，可以使用if type(dog) == type(cat):
print(type(dog.run) == types.FunctionType)  #type内置了的判断是否为函数的常量
print(type(abs) == types.BuiltinFunctionType)  #判断内置函数
print(type(lambda x: x) == types.LambdaType)  #判断匿名函数
print(type((x for x in range(10))) == types.GeneratorType)  #判断生成器

#isinstance()函数
print(isinstance([1, 2, 3], (list, tuple)))  #一次判断多个类型条件

#dir()函数，获取一个对象中的所有属性和方法，返回一个字符串成员组成的list
print(dir('123'))

#__len__()方法，在Python内置对象中一般含有这个方法，返回对象的长度。使用内置len()函数，等同于：
print(len('ABC'))
print('ABC'.__len__())

#getattr()函数，获取对象属性值，若不存在返回第三个形参
print(getattr(bart, 'name', 404))

#setattr()函数，给对象设置一个属性
setattr(bart, 'y', 9)
print(bart.y)

#hasattr()函数，检查一个对象中是否有该属性
print(hasattr(bart, 'y'))



print('\n\n\033[0;31;40m-6-------实例属性和类属性---------------------------------\033[0m')
#在类中可以使用self属性去创建属性，在该类的对象中使用'.'或setattr()函数也可以新建属性，这种属性称为'实例属性'
#在类中直接定义一个属性，称之为'类属性'
#一个类若拥有同名实例属性和类属性，该类对象的实例属性调用优先级会高于类属性
class Student(object):
    name = 'Student'

s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
#Student
print(Student.name) # 打印类的name属性
#Student
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
#Michael
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
#Student
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
#Student
