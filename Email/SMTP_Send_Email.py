#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1------SMTP发送邮件-------------------------------\033[0m')
#MUA：Mail User Agent——邮件用户代理
#MTA：Mail Transfer Agent——邮件传输代理
#MDA：Mail Delivery Agent——邮件投递代理
#1、设置邮件地址等等；2、创建邮件内容；3、发送

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):  #用于格式化一个邮件地址，使其变为
    name, addr = parseaddr(s)  #用来解析字符串中的email地址，使其用户名和地址分开，产生一个tuple
    #print('!!!!!', formataddr((Header(name, 'utf-8').encode(), addr)))
    return formataddr((Header(name, 'utf-8').encode(), addr))  #用Header函数编码收发件人的名称

#一、邮件设置部分
from_addr = 'xxxxxx@163.com'  #输入发件人Email地址
password = 'xxxxxxxxxxxx'  #密码
to_addr = 'xxxxxxxxx@qq.com'  #输入收件人地址:
smtp_server = 'smtp.163.com'  #输入SMTP服务器地址:

#二、邮件内容部分
##1、发送文本邮件
msg = MIMEText('邮件正文...', 'plain', 'utf-8')

##2、发送HTML邮件
#msg = MIMEText('<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 'html', 'utf-8')

##3、发送附件，构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可
'''
msg = MIMEMultipart()
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))  #附上邮件正文
with open('./taylor.jpg', 'rb') as f:  #添加附件
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='taylor.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='taylor.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
'''

##4、发送图片内容，未学会
'''
msg = MIMEMultipart()
msg.attach(MIMEText('send with file...', 'html', 'utf-8'))  #附上邮件正文
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
'''

##5、同时支持HTML和Plain格式(收件人使用的设备太古老，查看不了HTML邮件)
'''
msg = MIMEMultipart('alternative')  #无法查看HTML格式的邮件，就自动降级查看纯文本邮件
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 'html', 'utf-8'))
'''

msg['From'] = _format_addr('Python <%s>' % from_addr)  #发件人名称，目前发现必须添加标题、发件人名称才不容易进入垃圾箱（之前的shell发送email也需要这两点）
msg['To'] = _format_addr('Receive <%s>' % to_addr)  #收件人名称
msg['Subject'] = Header('邮件标题helloworld', 'utf-8').encode()  #标题，Header()函数用于编码文本，包含utf-8编码信息和Base64编码的文本

#三、发送执行部分
server = smtplib.SMTP(smtp_server, 25)  #SMTP协议默认端口是25
server.set_debuglevel(1)  #打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)  #登录
server.sendmail(from_addr, [to_addr], msg.as_string())  #第二个变量可以传入一个list发送给多个人，第三个变量是一个str类型的邮件正文
server.quit()


############################################################################################


#附shell脚本发送email代码：
#注意，使用该脚本前必须先安装sendEmail软件：sudo apt-get install sendemail
'''
#!/bin/bash
#使用qq邮箱进行发送需要注意：首先需要开启：POP3/SMTP服务
#其次发送邮件的密码需要使用在开启POP3/SMTP服务时候腾讯提供的第三方客户端登陆码。

#邮件设置部分
email_reciver=qqqqqq@qq.com  #收件人邮箱
email_sender=xxxxxx@163.com  #发送者邮箱
email_username=xxxxxx  #发送者邮箱用户名
email_password=yyyyyy  #邮箱密码
email_smtphost=smtp.163.com  #smtp服务器地址

#邮件内容部分
email_title="IP信息"
email_content=`curl http://members.3322.org/dyndns/getip`  #用于获得当前外网的ip地址作为邮件内容的一部分

#file1_path="附件一路径"
#file2_path="附件二路径"

#发送执行部分
sendemail -f ${email_sender} -t ${email_reciver} -s ${email_smtphost} \
-u ${email_title} -xu ${email_username} -xp ${email_password} \
-m ${email_content} -o message-charset=utf-8
'''


############################################################################################


#附C语言发送email代码(Ubuntu环境下)
'''
#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

using namespace std;

#define EHLO "EHLO helloworld\r\n"  //定义发件人邮箱用户名
#define DATA "data\r\n"
#define QUIT "QUIT\r\n"

int sock;
struct sockaddr_in server;
struct hostent *hp, *gethostbyname();
char buf[BUFSIZ + 1];
int len;

string host_id("smtp.163.com");  //发送者SMTP服务器地址
string from_id("xxxxxx@163.com");  //发送者邮箱
string from_id_base64("xxxxxxxxxxxxxxxxxx");  //发送者邮箱的base64编码
string from_password_base64("xxxxxxxxxxxxxxxxxxxxxx");  //发送者密码的base64编码
string to_id("qqqqqq@qq.com");  //接收者邮件
string sub("hello,This is 1\r\n");  //标题
string wkstr("Gold underperforms when real interest rates are positive and rising& that 's why gold had its worst January in twenty years.\r\n");  //内容

/*Send a string to the socket*/
void send_socket(string s)
{
  write(sock, s.c_str(), s.size());
}

/*Read a string from the socket*/
void read_socket()
{
  len = read(sock, buf, BUFSIZ);
  write(1, buf, len);
}

int main(int argc, char* argv[])
{
  /*Create Socket*/
  sock = socket(AF_INET, SOCK_STREAM, 0);
  if (sock == -1)
  {
    perror("opening stream socket");
    return 1;
  }
  else
    printf("socket created\n");

  /*Verify host*/
  server.sin_family = AF_INET;
  hp = gethostbyname(host_id.c_str());
  if (hp == (struct hostent *) 0)
  {
    fprintf(stderr, "%s: unknown host\n", host_id.c_str());
    return 2;
  }

  /*Connect to port 25 on remote host*/
  memcpy((char *) &server.sin_addr, (char *) hp->h_addr, hp->h_length);
  /*SMTP PORT*/
  server.sin_port = htons(25);
  if (connect(sock, (struct sockaddr *) &server, sizeof server) == -1)
  {
    perror("connecting stream socket");
    return 1;
  }
  else
    printf("Connected\n");

  /*Write some data then read some*/
  /*SMTP Server logon string*/
  read_socket();
  /*introduce ourselves*/
  send_socket(EHLO);
  /*Read reply*/
  read_socket();

  /*added by fupeng*/
  send_socket("AUTH LOGIN");
  send_socket("\r\n");
  read_socket();
  send_socket(from_id_base64);
  send_socket("\r\n");
  read_socket();
  send_socket(from_password_base64);
  send_socket("\r\n");
  read_socket();

  send_socket("mail from <");
  send_socket(from_id);
  send_socket(">");
  send_socket("\r\n");
  /*Sender OK*/
  read_socket();

  /*Mail to*/
  send_socket("rcpt to <");
  send_socket(to_id);
  send_socket(">");
  send_socket("\r\n");
  /*Recipient OK*/
  read_socket();

  /*body to follow*/
  send_socket(DATA);
  read_socket();
  send_socket("subject:");
  send_socket(sub);
  send_socket("\r\n\r\n");
  send_socket(wkstr);
  send_socket(".\r\n");
  read_socket();
  /*quit*/
  send_socket(QUIT);
  /*log off*/
  read_socket();

  /*Close socket and finish*/
  close(sock);
  return 0;
}
'''