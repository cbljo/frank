#!/usr/bin/env python

class bird(object):
	have_feather=True
	way_of_reproduction='egg'
	def mov(self,dx,dy):
		position=[0,0]
		position[0]=position[0]+dx
		position[1]=position[1]+dy
		return position


summer=bird()
print(summer.have_feather,'after move:',summer.mov(5,8))


class chicken(bird):
        way_of_move='walk'
        possible_in_KFC=True

class oriole(bird):
        way_of_move='fly'
        possible_in_KFC=False

summer=chicken()
print(summer.have_feather,'after move:',summer.mov(5,8))

class human(object):
        laugh='233333333'
        def __init__(self):
                print('just a test')
        def show_laugh(self):
                print self.laugh
        def laugh_10th(self):
                for i in range(10):
                        self.show_laugh()

lilei=human()
lilei.laugh_10th()
