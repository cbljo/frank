#!/usr/bin/env python

s='abcdefghijklmn'
for i in range(0,len(s),2):
    print(s[i])

for (index,char) in enumerate(s):
    print(index)
    print(char)
ta=[1,2,3]
tb=[4,5,6]
tc=['a','b','c']

for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)

f=open('iotest.txt','r')
a=0
try:
    while f.next():   #loop object
        a+=1
        print(a)
except:
    print('stop')

def gen():
    a=100
    yield a
    a=a*8
    yield a
    yield 1000

for i in gen():  #generator
    print i

def gen():
    for i in range(4):
        yield i

g=(x for x in range(4))  #generator expression

print(g) #g is a generator

for i in g:
    print i

l=[]
for x in range(10):
    l.append(x**2)
print(l)
l=[x**2 for x in range(10)]
print(l)

func=lambda x,y:x+y  #simple function
print(func(3,4))

def test(f,a,b):
    print('test')
    print(f(a,b))

test(func,3,5)
test((lambda x,y:x**2+y),6,9)

re=map((lambda x,y:x**2+y),[1,2],[3,4])
print(re)

def func(a):
    if a>100:
        return True
    else:
        return False

print (filter(func,[10,56,101,500]))

print(reduce((lambda x,y:x+y),[1,2,3,4,5,6,7]))  #cant be used after 3.x version, should import functools modules


