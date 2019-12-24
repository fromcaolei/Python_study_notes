#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------使用mysql------------------------\033[0m')
#先安装MySQL驱动
#sudo pip install mysql-connector-python --allow-external mysql-connector-python
#允许mysql远程连接
#mysql -u root -p
#use mysql;
#update user set host = '%' where user = 'root';
#select host,user from user;  --查看root用户的host列是否被改为%，允许root用户远程登录
#sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf  #注释bind-address		= 127.0.0.1行，重启mysql服务完成

'''
import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='test')  #连接mysql
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')  #创建user表
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])  #给user表插入一行数据，MySQL的SQL占位符是%s
print(cursor.rowcount)
conn.commit()  #提交保存到数据库
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))  #查询id列为1的行
values = cursor.fetchall()  #拿到结果集，结果集是一个list，每个成员都是一个tuple
print(values)
cursor.close()
conn.close()
'''

print('\n\n\033[0;31;40m-2--------使用SQLAlchemy------------------------\033[0m')
#类似C#代码结构中的model实体对象
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,PrimaryKeyConstraint

Base = declarative_base()  #创建对象的基类，用于定义实体类的父类来源于此

class new_table(Base):  #定义test_table对象
    __tablename__ = 'new_table'  #表的名字
    id = Column(String(20), primary_key=True)  #表的结构，这里定义的变量名一定要和表内列明对应上
    #id = Column(Integer, name='id', primary_key=True)  #另一种可行写法
    first = Column(String(50))


engine = create_engine('mysql+mysqlconnector://root:toor@127.0.0.1:3306/my_test')  #初始化数据库连接
DBSession = sessionmaker(bind=engine)  #创建DBSession类型

'''
#数据表写入一行
session = DBSession()  #创建session对象
new_user = User(id='5', name='Bob')  #创建新User对象
session.add(new_user)  #添加到session
session.commit()  #提交即保存到数据库
session.close()  #关闭session
'''

#数据表查询一行
session = DBSession()  #创建Session
test = session.query(new_table).filter(new_table.id=='1').one()  #创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
print('type:', type(test))  #打印类型和对象的name属性
print('first:', test.first)
session.close()  #关闭Session










#数据表生成SQL文档
'''
-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: my_test
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `my_test`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `my_test` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE `my_test`;

--
-- Table structure for table `new_table`
--

DROP TABLE IF EXISTS `new_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_table`
--

LOCK TABLES `new_table` WRITE;
/*!40000 ALTER TABLE `new_table` DISABLE KEYS */;
INSERT INTO `new_table` VALUES (1,'one'),(2,'two');
/*!40000 ALTER TABLE `new_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-19 21:03:54
'''