# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:37:02 2017

@author: yuweili
"""

import threading
import time
import os
import random

def check():
    time.sleep(1)
    
class bt(threading.Thread):
    def __init__(self,wid,monitor):
        self.wid = wid
        self.monitor=monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].acquire()
            if monitor['done'] < 10:
                monitor['done']+=1
                check()
                print (self.wid,'have done the work,%d now'%monitor['done'])
            elif monitor['done']==10:
                monitor['done']+=1
                check()
                print('bierzeit')
            elif monitor['done']<20:
                monitor['done']+=1
                check()
                print(self.wid,'have done the work,%d now'%monitor['done'])
            else:
                print('done')
                os._exit(0)
            monitor['lock'].release()
    
monitor={'done':0,'lock':threading.Lock()}
    
for k in range(20):
    nt=bt(k,monitor)
    nt.start()