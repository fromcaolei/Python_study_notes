print('\n\n\033[0;31;40m-1--------切片-------------------------------------------------\033[0m')
#切片，一种截取list、tuple、字符串等类型的操作符':'，类似C#中Substring()
L = list(range(11))
print(L)
print(L[0:3])  #截取前3个，不包括3的元素，也支持从负值开始即：L[-1:10]得到10
print(L[0:7:2])  #每隔2个截取一个,到第七个元素为止

print((0, 1, 2, 3, 4, 5)[:3])  #对tuple使用,':'前面不谢值等同于0

print('ABCDEFG'[:3])  #对字符串使用



print('\n\n\033[0;31;40m-2--------迭代-------------------------------------------------\033[0m')
#属于for...in循环的使用方式补充
#dict类型：
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)  #默认dict迭代key

for value in d.values():
    print(value)  #迭代value

for k, v in d.items():
    print(k, v)  #迭代整个元素

#字符串类型：
for ch in 'ABC':
    print(ch)

#list类型，将元素和角标一起迭代出来，适用enumerate()函数
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

#判断一个对象是否可被迭代，使用collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc', Iterable))  #可以迭代
print(isinstance(123, Iterable))  #不能迭代



print('\n\n\033[0;31;40m-3--------列表生成式-------------------------------------------\033[0m')
#用来生成一些有规律list的语法，减少for循环的使用

#生成[1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1, 11)])  #把要生成元素的公式写在前方，后面跟for循环即可，注意前面公式中的变量和迭代中的变量要一致

#使用两层for循环
print([m + n for m in 'ABC' for n in 'XYZ'])

#生成当前目录下所有文件
import os
print([d for d in os.listdir('.')])

#使用两个变量生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

#把list中的所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])



print('\n\n\033[0;31;40m-4--------生成器-----------------------------------------------\033[0m')


