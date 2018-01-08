#!/bin/bash

#使用前线设置/etc/network/interfaces文件中的内容为(ubuntu12.04)：
#auto lo
#iface lo inet loopback

#auto eth0
#iface eth0 inet static
#address 172.16.51.25
#netmask 255.255.255.0
#gateway 172.16.51.254



echo -e 'hello world!'

ping -c 4 172.16.51.159
if [ $? == '1' ];then
    echo 'f' | sudo -S ifconfig eth0 172.16.51.159 netmask 255.255.255.0
    echo 'f' | sudo -S route add default gw 172.16.51.254
    echo 'f' | sudo -S ntpdate 91.189.91.157
    echo 'f' | sudo -S /etc/init.d/networking restart
    echo "更新时间成功！"
else
    echo "该IP正在使用，暂时不能更新时间"
fi
