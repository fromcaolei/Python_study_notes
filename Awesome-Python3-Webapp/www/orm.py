#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

import asyncio, logging

import aiomysql

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

@asyncio.coroutine
#创建数据库连接池
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool  #定义一个全局变量用于存放数据库连接池对象，在函数执行前首先执行，并且永远会被执行
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),  #如果键名不存在，不想返回None就返回一个自己想要的参数localhost
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),  #从数据库中获取到的数据按照UTF-8编码读取，中文不会出错
        autocommit=kw.get('autocommit', True),  #是否自动提交事物，默认true自动
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

@asyncio.coroutine
#查询语句，第一个参数为sql语句,第二个为sql语句中占位符的参数列表,第三个参数是要查询数据的数量，返回值为多维元组
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:  #定义__pool为aiomysql库中的，所以需要异步调用
        cur = yield from conn.cursor(aiomysql.DictCursor)  #DictCursor这个模块可以使通过字段名获取对应的值
        yield from cur.execute(sql.replace('?', '%s'), args or ())  #replace用于将?替换为%s
        if size:
            rs = yield from cur.fetchmany(size)  #fetchmany函数用于设置获得表中的多少数据使用
        else:
            rs = yield from cur.fetchall()  #fetchall函数返回所有结果，多维tuple，如(('id','title'),('id','title')),
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs  #多维tuple，查询到的数据结果

@asyncio.coroutine
#增删改语句，第一个参数为sql语句,第二个为sql语句中占位符的参数列表,第三个参数是自动提交事物，默认true自动，返回值为影响的行数
def execute(sql, args, autocommit=True):
    log(sql)
    with (yield from __pool) as conn:
        if not autocommit:
            yield from conn.begin()  #开启事务
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount  #获得sql语句影响的行数
            yield from cur.close()
            if not autocommit:
                yield from conn.commit()  #提交事务
        except BaseException as e:
            if not autocommit:
                yield from conn.rollback()  #回滚事务，在执行commit()之前如果出现错误,就回滚到执行事务前的状态,以免影响数据库的完整性
            raise
        return affected  #返回影响的行数

#创建拥有num个占位符的字符串
def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)  #用于将序列中的元素以", "连接生成一个新的字符串

#保存数据库列名和类型的基类
class Field(object):

    def __init__(self, name, column_type, primary_key, default):
        self.name = name  #定义列名属性
        self.column_type = column_type  #列类型
        self.primary_key = primary_key  #是否为主键
        self.default = default  #默认值

    def __str__(self):  #用于将对象转化为适于人阅读的形式，可以使用str(obj)函数调用到该私有函数
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


#定义多个相应的字段类型，调用父类方法的构造函数
class StringField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)

class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)

class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)

class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)

#定义一个元类，用于被model类继承，ORM框架的惯用手法
class ModelMetaclass(type):
    #__new__函数用来指导如何生成类的实例，比__init__更早的被调用，和__init__区别：__new__中我们通常只是修改dct，但是在__init__中，我们可以直接修改创建好的类
    #第一个参数cls是将要创建的类，指向的是class；第二个参数是所定义类的名字，通常用类名.__name__获取；第三个是基类；第四个是dict类型，包含所定义类的属性或函数
    def __new__(cls, name, bases, attrs):
        if name=='Model':  #如果所创建的类是Model类，不做处理
            return type.__new__(cls, name, bases, attrs)

        tableName = attrs.get('__table__', None) or name  #通过dict提供的get()方法确定key的存在，可返回指定结果，若不存在__table__键，则将所定义的类名当做表名保存
        logging.info('found model: %s (table: %s)' % (name, tableName))

        mappings = dict()  #创建一个字典类型的变量，保存所有"列属性"
        fields = []  #创建一个list类型的变量，保存不是主键列的"列属性名"
        primaryKey = None  #保存主键列属性的"列属性名"

        for k, v in attrs.items():  #将所定义类的每个属性遍历，items()将dict对象转换成了包含tuple的list
            if isinstance(v, Field):  #如果属性是个列名（field类在上方以声明过，用于存储列名和数据类型）
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v  #将所有"列属性"保存到字典变量中
                if v.primary_key:  #如果这个列是主键列
                    if primaryKey:  #若之前已经找到过一个主键列，则数据表异常
                        raise StandardError('Duplicate primary key for field: %s' % k)
                    primaryKey = k  #保存主键列"列属性名"到主键列变量中
                else:
                    fields.append(k)  #将不是主键列的"列属性名"追加到list变量的末尾
        if not primaryKey:
            raise StandardError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)  #删除所定义类的所有"列属性"元素
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))  #利用map将不是主键的列"列属性名"做成类似：['`k1`', '`k2`', '`k3`']
        attrs['__mappings__'] = mappings  #给所定义类创建新私有属性__mappings__,保存属性和列的映射关系
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey  #主键"列属性名"
        attrs['__fields__'] = fields  #除主键外的"列属性名"
        #以下四种方法保存了默认了增删改查操作,其中添加的反引号``,是为了避免与sql关键字冲突的,否则sql语句会执行出错
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):若调用一个不存在的键，则弹出这个默认值
        super(Model, self).__init__(**kw)  #继承了dict类，构造时也调用了这个父类的构造函数，就会在创建对象时，要求你输入字典形式的参数列表

    def __getattr__(self, key):  #对调用到不存在的属性或函数时，会调用该函数，若该属性在类中已经是键值对，则该方法可通过下标[key]来取值（言简意赅的说，就是通过该函数实现了用点语法(".")获取字典中某键的值）
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):  #同上，通过该函数实现了用点语法(".")设置字典中某键的值
        self[key] = value

    def getValue(self, key):  #通过下标[key]来取值的函数
        return getattr(self, key, None)

    def getValueOrDefault(self, key):  #若调用一个不存在的键，则弹出这个默认值
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod  #这个修饰器可是这个函数调用可通过类名直接调用，而不需要生成对象去调用，即定义类的类方法
    @asyncio.coroutine
    def findAll(cls, where=None, args=None, **kw):  #第一个参数表示自身类
        ' find objects by where clause. '
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = yield from select(' '.join(sql), args)  #一上代码配合类中原有的select语句，追加where及之后语句，时sql查询语句完整，异步调用select()函数获得结果多维tuple
        return [cls(**r) for r in rs]  #！！！这个列表生成式表示没看懂cls(**r)的结果是什么？？？

    @classmethod
    @asyncio.coroutine
    def findNumber(cls, selectField, where=None, args=None):
        ' find number by select and where. '
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = yield from select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    @asyncio.coroutine
    def find(cls, pk):
        ' find object by primary key. '
        rs = yield from select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    @asyncio.coroutine
    def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = yield from execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    @asyncio.coroutine
    def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = yield from execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)

    @asyncio.coroutine
    def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = yield from execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)
