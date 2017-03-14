#!/usr/bin/env python

f=open('new test','w')
print(f.closed)
f.write('hello world')
f.close()
print(f.closed)

with open('new test2','w') as f:
    print(f.closed)
    f.write('hello world')
print(f.closed)
