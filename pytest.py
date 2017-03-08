#!/usr/bin/env python

print('hello world!')
a=10
def pt(a):
	b=[a,type(a)]
	print(b)
pt(a)
a=1.3
pt(a)
b=True
pt(b)
c='hello'
pt(c)
da=(1,2,3)
pt(da)
ea=[1,2,3,4,5,6,7,8,9,0]
pt(ea)
print(ea[1])
print(ea[0:5:2])
print(c[2:4])
print(1+9,1.3-4,3*5,4.5/1.5,3**2,10%3)
print(5==6,8!=8,3<=3,3<3,5 in [1,3,5])
print(True and True,True or False,not True)

for i in range(0,20):
	if i %3:
		print('type 1',i)
	else:
		print('type 3',i)


a=0
while a<=20:
	if not a%2:
		a+=1
		continue
	if a==15:
		break
	print(a)
	a+=1


