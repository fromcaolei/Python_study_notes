#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\n\n\033[0;31;40m-1--------常用第三方模块------------------------------\033[0m')
print('\n\n\033[0;31;40m-2--------Pillow------------------------------------\033[0m')
#一个图像处理的库
from PIL import Image, ImageFilter, ImageDraw, ImageFont  #ImageFilter用来加滤镜，ImageDraw用来绘图，ImageFont用来在图片中定义字体

im = Image.open('./taylor.jpg')  #打开一个jpg图像文件
w, h = im.size  #获得图像尺寸，返回一个tuple
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))  #缩放到50%，//表示取整
print('Resize image to: %sx%s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')  #把缩放后的图像用jpeg格式保存:


im2 = im.filter(ImageFilter.BLUR)  #应用模糊滤镜，filter()函数本身不会改变图像，可使用其返回值保存新图像
im2.save('blur.jpg', 'jpeg')


#一个生成字母验证码的例子，方式有点类似C#中的GDI+技术
import random  #用于可以使用生成随机数的函数random()
def rndChar():  #随机字母生成
    return chr(random.randint(65, 90))

def rndColor():  #随机颜色1
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():  #随机颜色2
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('./Arial.ttf', 36)  #创建Font对象

draw = ImageDraw.Draw(image)  #创建Draw对象

for x in range(width):  #填充每个像素（背景图）
    for y in range(height):
        draw.point((x, y), fill=rndColor())

for t in range(4):  #输出文字（背景图上写字）
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)  #加模糊
image.save('code.jpg', 'jpeg')



print('\n\n\033[0;31;40m-3--------requests--------------------------------\033[0m')
#类似与常用內建模块中的urllib模块，但功能较为高级好用
import requests

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})  #请求带参数的url，也可输入一个普通的url
print(r.status_code)
#print(r.headers)  #获取响应头
#print(r.text)
print(r.url)  #获得完整链接
print(r.encoding)  #检查编码
#print(r.content)  #获得bytes对象的内容
#print(r.cookies['ts'])  #不必解析Cookie就可以轻松获取指定的Cookie
r = requests.get(r.url, timeout=2.5)  #指定超时，2.5秒后超时

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')  #请求一个类型的响应
#print(r.json())

r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})  #传入HTTP Header的方法

r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})  #发送POST请求

params = {'key': 'value'}
r = requests.post(r.url, json=params)  #传递JSON数据，内部自动序列化为JSON

#upload_files = {'file': open('report.xls', 'rb')}  #传送文件，更复杂的编码格式。务必使用'rb'即二进制模式读取
#r = requests.post(url, files=upload_files)

cs = {'token': '12345', 'status': 'working'}
r = requests.get(r.url, cookies=cs)  #请求中传入cookies参数