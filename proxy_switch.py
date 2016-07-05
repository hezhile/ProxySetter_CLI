#!/usr/bin/env python
#coding=utf-8

import winreg
import sys
import json
import os

print ("代理服务器设置助手 2.2 Build20140714")
print ("")
print("注意：修改代理设置前，请先关闭Internet Explorer！")
print ("")
print ("当前设置")
handle = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Internet Settings")
current_proxy_server = winreg.QueryValueEx(handle, "ProxyServer")
proxy_server_status = winreg.QueryValueEx(handle, "ProxyEnable")
status=('否','是')
print ("代理服务器地址和端口：",current_proxy_server[0])
print ("启用状态：",status[proxy_server_status[0]])
print ("")

def set_proxy(addr,port,bit):
    handle2 = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Internet Settings", reserved=0, access=winreg.KEY_SET_VALUE)
    winreg.SetValueEx(handle2,'ProxyServer',0,1,addr+':'+port)
    winreg.SetValueEx(handle2,'ProxyEnable',0,4,bit)


def mod_menu(menu_content):
    menu_length = len(menu_content)
    menu_entry = sorted(menu_content.keys())
    for i in menu_entry:
        print (i+'--'+menu_content[i][0])
    print ('x--退出')
    print ('')
    try:
        choice = input("请输入: ")
    except:
        choice = 'wrong'
    if choice in menu_entry:
        set_proxy(menu_content[choice][1],menu_content[choice][2],menu_content[choice][3])
        print ('done! 再见～')
    else:
        print ("再见～")
        sys.exit()

file_target = 'config.txt'

def file_test():
    if not(file_target in os.listdir()):
        print ("找不到配置文件，使用默认配置，再见～")
        set_proxy('172.16.217.240', '3128', 1)
        file_handle=open(file_target,'w')
        default_proxy={"1": ["内网代理", "172.16.216.240", "3128", 1]}
        json.dump(default_proxy,file_handle)
        file_handle.close()
        sys.exit()
    return

def read_file(target):
    file_handle=open(target,'r')
    config_str=json.load(file_handle)
    file_handle.close()
    return config_str

file_test()
config_str=read_file(file_target)
mod_menu(config_str)
