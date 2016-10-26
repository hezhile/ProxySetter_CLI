#!/usr/bin/env python
#coding=utf-8

import winreg
import sys
import json
import os

print ("ProxySetter CLI V2.3 Build20160715")
print ("")
print("Attention: Please close Internet Explorer first.")
print ("")
print ("==Current settings==")
handle = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Internet Settings")
proxy_server_status = winreg.QueryValueEx(handle, "ProxyEnable")
if proxy_server_status[0]:
    current_proxy_server = winreg.QueryValueEx(handle, "ProxyServer")
    print ("Proxy server: ",current_proxy_server[0])
status=('No','YEs')

print ("enabled: ",status[proxy_server_status[0]])
print ("")

def set_proxy(addr,port,bit):
    handle2 = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Internet Settings", reserved=0, access=winreg.KEY_SET_VALUE)
    winreg.SetValueEx(handle2,'ProxyServer',0,1,addr+':'+port)
    winreg.SetValueEx(handle2,'ProxyEnable',0,4,bit)


def mod_menu(menu_content):
    menu_length = len(menu_content)
    menu_entry = sorted(menu_content.keys())
    for i in menu_entry:
        print (i+' -- '+menu_content[i][0])
    print ('x -- Exit')
    print ('')
    try:
        choice = input("Enter: ")
    except:
        choice = 'wrong'
    if choice in menu_entry:
        set_proxy(menu_content[choice][1],menu_content[choice][2],menu_content[choice][3])
        print ('done! Bye')
    else:
        print ("Good Bye")
        sys.exit()

file_target = 'config.txt'

def file_test():
    if not(file_target in os.listdir()):
        print ("configuration file no found, load the default settings, bye.")
        set_proxy('172.16.217.240', '3128', 1)
        file_handle=open(file_target,'w')
        default_proxy={"1": ["HTTP Proxy", "172.16.216.240", "3128", 1]}
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
