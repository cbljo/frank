# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:18:56 2017

@author: yuweili
"""

import threading
import time
import os

# This function could be any function to do other chores.
def doChore():
    time.sleep(0.5)

# Function for each thread
class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid          = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].acquire()                          # Lock; or wait if other thread is holding the lock
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1          # Sell tickets
                print(self.tid,':now left:',monitor['tick'])   # Tickets left
                doChore()                                      # Other critical operations
            else:
                print("Thread_id",self.tid," No more tickets")
                os._exit(0)    
                monitor['lock'].release()                          # Unblock
            doChore()                                          # Non-critical operations

# Start of the main function
monitor = {'tick':100, 'lock':threading.Lock()}

# Start 10 threads
for k in range(10):
    new_thread = BoothThread(k, monitor)
    new_thread.start()
