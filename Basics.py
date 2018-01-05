#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第二行告诉解释器按照UTF-8编码读取源码，中文不会出错

print('\n\n\033[0;31;40m-1--------print()函数---------------------------------------------------\033[0m')
#print()函数
print(100+200+300)
print("你好！")
print('100 + 200 =', 100 + 200)
print('''line1
line2
line3''')  #打印多行
print('Hi,%s,you have $%d.' %('Michael', 1000000))  #补3个0使用%03d，补2个空格使用%2d，小数保留2位%.2f，使用%s会把任何数据转换成字符串，使用%%会打印%本身

#可以使用input()函数来输入，name = input()


print('\n\n\033[0;31;40m-2---------代码缩进------------------------------------------------------\033[0m')
#以#开头为注释，以：结尾为时缩进的语句为代码块
a = 100
if a >= 0:
    print(a)
else:
    print(-a)


print('\n\n\033[0;31;40m-3---------字符串和编码 ord()函数 chr()函数------------------------------\033[0m')
#字符串和编码
print(ord("中"))  #获取字符的整数表示
print(chr(25991))  #将编码转换为对应字符
print('\u4e2d\u6587')  #以\u加16进制数可直接获得对应编码的字符串


print('\n\n\033[0;31;40m-4-------byte类型---字符串的encode()函数---------------------------------\033[0m')
#byte类型用b'_'表示
#encode()函数，将Unicode表示的字符串转换为byte类型
print('ABC'.encode('ascii'))  #英文用ascii编码为byte类型
print('中文'.encode('utf-8'))  #将中文用utf-8编码为byte类型


print('\n\n\033[0;31;40m-5-------字符串的decode()函数--------------------------------------------\033[0m')
#decode()函数，将byte转换为字符串
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))  #忽略错误的字节


print('\n\n\033[0;31;40m-6--------len()函数------------------------------------------------------\033[0m')
#len()函数，计算字符数
print(len('中文'))  #2
print(len('中文'.encode('utf-8')))  #6


print('\n\n\033[0;31;40m-7--------list类型-------------------------------------------------------\033[0m')
#list是一种有序的集合，类似于C中的数组，可以随时添加和删除其中的元素，下面的classmates是一个变量，不是关键字,其内部的数据类型也可以不同
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))  #可以使用len()计算list中的成员个数
print(classmates[0])  #list的索引从0开始计算，类似C中的数组
print(classmates[-1])  #索引为-1时，可以调用list中的最后一个元素,-2调用倒数第二个依次类推

classmates.append('Adam')  #append()追加元素到list末尾
print(classmates)

classmates.insert(1, 'Jack')  #insert()插入元素到索引1的位置
print(classmates)

classmates.pop()  #pop()会删除指定索引位置的元素，为空时删除末尾元素
print(classmates)

classmates[1] = 'Sarah'  #替换元素时，可以直接给某成员赋值
print(classmates)

p = ['asp', classmates, 'php']
print(p)


print('\n\n\033[0;31;40m-8--------tuple类型------------------------------------------------------\033[0m')
#tuple叫做元组，类似于list，类似于const数组，但一旦初始化就不能更改,没有append()，insert()方法，也不能给成员二次赋值。注意：若成员中有list成员，那么这个list成员内部的元素可以发生变化
tuplemates = ('Michael', 'Bob', 'Tracy')
print(tuplemates)

s = (1.2212)  #注意，若定义只有一个成员的tuple且值为一个数时，需要在其后面加一个逗号（1，），否则会当做一个数去处理tuple
print(s)  #终端打印时，不会出现括号


print('\n\n\033[0;31;40m-9--------条件判断-------------------------------------------------------\033[0m')
#if判断语句由上往下判断，在某个判断为true时，以下的elif判断内容均不执行，同C一样。当判断条件为一个非零数或非空list、字符串时，也触发true判断。

age = 3
#age = input('请输入一个数字：')
#age = int(age)
if age >= 18:
    print('your age is', age)
    print('adult')  #这个print满足缩进规则
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('kid')


print('\n\n\033[0;31;40m-10--------循环----------------------------------------------------------\033[0m')
#for...in循环，将条件中的list依次迭代出来，类似C#中的foreach
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

print( list(range(5)) )  #range()函数生成一个整数序列，可使用list()函数将其生成list，可在for循环中使用

#while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#break语句，用来提前退出循环
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

#continue语句，用来跳过本次循环
n = 0
while n <= 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)



print('\n\n\033[0;31;40m-11------- dict类型------------------------------------------------------\033[0m')
#dictionary类似C++中的map，C#中的Dictionary类，key不可以有重复值，若有将会自动覆盖前面的键值对。查询时间快，占内存插入慢。key部分不可以放入可变对象，如list，可以是数字或字符串
a = 'Michael'
d = {a:95, 'Bob':75, 'Tracy':85}
a = 'Bob'
print(d,'\n',a)

print(d[a], d['Michael'])  #通过key查找
d['Adam'] = 67  #通过key插入值 和 覆盖之前的值
print(d)

print('Thomas' in d)  #通过in判断是否有这个key
print('Bob' in d)
print(d.get('Thomas', '并不存在这个值'))  #通过dict提供的get()方法确定key的存在，可返回指定结果，未设置返回结果返回None

d.pop('Bob')  #通过key删除一个成员
print(d)



print('\n\n\033[0;31;40m-12------- set类型------------------------------------------------------\033[0m')
#set和dict也是一组key的集合，但无value，且key不重复，插入重复值就被自动过滤。不可以放入可变对象，如list，可以是数字或字符串
s = set([1, 2, 3])  #初始化时，需要一个list作为输入
print(s)

s.add(4)  #添加元素
print(s)

s.remove(4)  #删除元素
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  #可以执行数学意义上的交集、并集操作
print(s1 | s2)
