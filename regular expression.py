# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:57:38 2017

@author: yuweili
"""

#import re　#正则表达式
import time,datetime  #时间与日期
#import os.path,glob  #路径与文件
#import os,shutil  #文件管理
#import pickle,cPickle  #储存对象
import subprocess  #使用子进程
#=re.search('[0-9]','abcd4ef')
#print(m.group(0))
import signal  #ｐｙｔｈｏｎ程序内部处理信号
print(time.time())
print(time.clock())
print('start')
time.sleep(10)
print('wake up')
child=subprocess.Popen(["firefox","www.baidu.com"])
print("parent process")