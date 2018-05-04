#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
from models import User,Blog,Comment
import asyncio

async def test():

    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='toor',db='awesome')

    #没有设置默认值的一个都不能少
    #u = User(name='dflhuang', email='dflhuang@qq.com', passwd='0123', image='about:blank',id='111')
    #由于email是外键，所以每次email需要变化，否则保存时报错
    u = User(name='Test', email='test3@example.com', passwd='1234567890', image='about:blank')
    
    await u.save()
    await orm.destory_pool()  #新加入，关闭数据库连接池

# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())

#关闭EventLoop
loop.close()