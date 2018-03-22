#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------使用模板-------------------------------\033[0m')
#模板是将预先准备好的HTML文档嵌入一些变量和指令，然后传入数据替换，得到最终HTML。也就是MVC：Model-View-Controller(模型-视图-控制器)，包含变量的HTML为视图，Python处理URL的函数就是控制器，模型就是一个dict，键为HTML中的变量，值为程序中想要替换的值。

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')  #注意，这些HTML文件要放到名为templates的目录下，templates和该Python文件在同级目录

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='p':
        return render_template('signin-ok.html', username=username)  #Flask通过render_template()函数实现模板渲染，falsk默认支持的模板是jinja2
    return render_template('form.html', message='Bad username or password', username=username)  #由于HTML代码中加判断message值，所以当失败是给message赋值，并继续返回form.html文件即可弹出红色字，和继续该页面。

if __name__ == '__main__':
    app.run()


#在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
#比如循环输出页码，page_list是一个list：[1, 2, 3, 4, 5]，下面的模板将输出5个超链接。
'''
{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}
'''

'''
除了Jinja2，常见的模板还有：
Mako：用<% ... %>和${xxx}的一个模板；
Cheetah：也是用<% ... %>和${xxx}的一个模板；
Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
'''
