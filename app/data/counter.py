#!/usr/bin/env python
#coding: utf-8

from datetime import datetime, timedelta

class Counter(dict):
    def expire(self):
        
        #avoind the dot to performance
        now=datetime.now
        for k in self.keys():
            if self[k] < now():
                del(self[k])

    def incr(self, uid):
        #TODO: minutes must be on a conf file
        self[uid]=datetime.now()+timedelta(minutes=30)

    def count(self):
        return len(self.keys())
