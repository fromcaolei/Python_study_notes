#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------HTTP简介-------------------------------\033[0m')
#在浏览器的开发者工具中，选择network，再选第一条记录，右侧将显示Request Headers，点击右侧的view source，就可以看到浏览器发给服务器的HTTP请求

#请求部分：
'''
GET仅请求资源
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

POST会附带用户数据，包含一个body，以双\r\n分隔
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
'''

#响应部分：
#body内容也是通过双\r\n分隔，数据类型由Content-Type头来确定，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据
'''
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
'''
#内容：200表示一个成功的响应，后面的OK是说明。3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；


print('\n\n\033[0;31;40m-2--------HTML简介-------------------------------\033[0m')
#HTML
'''
<html>
<head>
  <title>Hello</title>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
'''

#CSS是Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现
'''
<html>
<head>
  <title>Hello</title>
  <style>
    h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
  </style>
</head>
<body>
  <h1>Hello, world!</h1>
</body>
</html>
'''


#JavaScript和Java一点关系没有，JavaScript是为了让HTML具有交互性而作为脚本语言添加的，JavaScript既可以内嵌到HTML中，也可以从外部链接到HTML中，有些类似C#为某控件添加事件的委托
'''
<html>
<head>
  <title>Hello</title>
  <style>
    h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
  </style>
  <script>
    function change() {
      document.getElementsByTagName('h1')[0].style.color = '#ff0000';
    }
  </script>
</head>
<body>
  <h1 onclick="change()">Hello, world!</h1>
</body>
</html>
'''


print('\n\n\033[0;31;40m-3--------WSGI接口-------------------------------\033[0m')
#
