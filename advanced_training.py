#!/usr/bin/env python

import modtest

dic={'tom':11,'sam':57,'lily':100}
print(dic,type(dic))
print(dic.items())
print(dic.keys())
print(dic.values())
dic['lilei']=99
print(dic)
del dic['tom']
print(dic)



for i in range(10):
    modtest.laugh()






f=open('iotest.txt','r')
a=f.read(10)
b=f.readlines()
print(a,b)
f.close()

e=file('write_test.txt','w')
e.write('this is a test\n')
e.write('2nd line\n')
e.close()

def func(*name):   #packing
    print(name,type(name))

func(1,4,6)
func(1,2,3,'abc')

def func2(a,b,c):
    print(a,b,c)
    print(a)

arg=(1,3,4)
func2(*arg)


