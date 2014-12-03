#coding=utf-8
from __future__ import division
import time

class Frequency:
    
    freq=None # how many timer by second
    started=None

    def __init__(self, frequency=1):
        self.freq=frequency 

    def start(self):
        self.started=time.time()

    def end(self):

        dt_by_item =  1/self.freq

        endtime = time.time()
        
        if endtime-self.started < dt_by_item:

            time.sleep( dt_by_item-(endtime-self.started) )
