#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------模块---------------------------------------------\033[0m')
#一个.py文件就称之为一个模块，为了避免模块重名，需要按目录来组织模块的方法，称为包。
#每个包下必须有一个__init__.py文件，否则这个目录就是一个普通目录，__init__.py可以是空文件。__init__.py本身就是一个模块
#调用包中的模块：mycompany.abc



print('\n\n\033[0;31;40m-2--------使用模块-----------------------------------------\033[0m')
' a test module '  #任何模块的第一个字符串都被视为文档注释

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, World')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()


#1、任何模块的第一个字符串都被视为文档注释
#2、当直接运行该模块时__name__的值为'__main__'，在其他地方导入该模块时，__name__的值将会变化，不再执行test()函数。
#3、模块中，函数和变量使用'_'、'__'前缀来定义私有private成员
#4、类似__xxx__这样的变量是特殊变量，可被直接引用，如：
#__author__(定义作者)、__name__(在运行时置为'__main__')、__doc__(模块定义的文档注释)
#5、安装第三方模块，需要知道第三方模块的名称，在pypi.python.org上可以找到。使用pip命令：pip install <name>   (安装Anaconda可以安装很多默认第三方库)
