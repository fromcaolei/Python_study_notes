#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------常用內建模块------------------------------\033[0m')
print('\n\n\033[0;31;40m-2--------datetime--------------------------------\033[0m')
#datetime，处理日期和时间的标准库
from datetime import datetime
now = datetime.now()
print(now)  #获取当前的datetime
print(datetime(2015, 4, 19, 12, 20))  #用指定日期创建datetime

print(now.timestamp())  #把datetime转换为timestamp，即从1970/1/1开始计算的时间
print( datetime.fromtimestamp( now.timestamp() ) )  #把timestamp转换为datetime
print(datetime.utcfromtimestamp(now.timestamp()))  #UTC时间，把timestamp转换为UTC时间

print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))  #把字符串转换为datetime
print(now.strftime('%a, %b %d %H:%M'))  #把datetime转换为字符串

from datetime import timedelta
print(now + timedelta(hours=10))  #datetime加减
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))  #创建时区UTC+8:00
print(now.replace(tzinfo=tz_utc_8))  #强行给datetime设置一个时区

#时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  #拿到UTC时间，并强制设置时区为UTC+0:00
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  #astimezone()将转换时区为北京时间
print(bj_dt)



print('\n\n\033[0;31;40m-2--------collections-----------------------------\033[0m')
#