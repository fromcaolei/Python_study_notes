#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------POP3收取邮件-----------------------------\033[0m')
#第一步：用poplib把邮件的原始文本下载到本地；第二步：用email解析原始文本，还原为邮件对象。

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

#一、邮件设置部分
email = 'zxc6982361@163.com'  #输入邮件地址, 口令和POP3服务器地址
password = 'zxc13379470731'
pop3_server = 'pop3.163.com'

#二、连接到目标MDA的pop3服务器
server = poplib.POP3(pop3_server)  #连接到POP3服务器
server.set_debuglevel(1)  #可以打开或关闭调试信息
print(server.getwelcome().decode('utf-8'))  #可选:打印POP3服务器的欢迎文字

server.user(email)  #身份认证
server.pass_(password)

print('Messages: %s. Size: %s' % server.stat())  #stat()返回邮件数量和占用空间
resp, mails, octets = server.list()  #list()返回所有邮件的编号,可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

index = len(mails)  #获取最新一封邮件, 注意索引号从1开始，这里index的值指向最后一封邮件
resp, lines, octets = server.retr(index)


msg_content = b'\r\n'.join(lines).decode('utf-8')  #lines存储了邮件的原始文本的每一行,可以获得整个邮件的原始文本
msg = Parser().parsestr(msg_content)  #稍后解析出邮件。这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层，要递归地打印出Message对象的层次结构。

#server.dele(index)  #可以根据邮件索引号直接从服务器删除邮件

server.quit()  #关闭连接:

#三、邮件解码部分
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg, indent=0):  #indent用于缩进显示
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

print_info(msg, indent=0)