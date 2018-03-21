#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------Flask框架-------------------------------\033[0m')
#在WSGI接口之上进一步抽象，专注于用一个函数处理一个URL，至于URL到函数的映射，交给Web框架来做。
#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
#以下实现网页localhost:5000的：
#GET /：首页，返回Home；GET /signin：登录页，显示登录表单；POST /signin：处理登录表单，显示登录结果

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='p':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()