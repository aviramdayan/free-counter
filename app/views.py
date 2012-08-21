# encoding: utf-8
import logging
from google.appengine.ext import webapp
from google.appengine.api import memcache


from data import counter

class Get(webapp.RequestHandler):
    def get(self):
        #TODO: put these fields/configurations on a conf file
        self.response.headers['Content-Type'] = 'text/x-javascript'
        site=self.request.get('s')
        uid = self.request.get('uid', '')
        if not site or not uid:
            return self.response.out.write('')

        status = memcache.get(site) or counter.Counter()
        #TODO: Expire must be on the Counter __init__
        status.incr(uid)
        status.expire()
        memcache.set(site, status)
        return self.response.out.write('__callback({"online": %s});' % 
                status.count())
