# encoding: utf-8
# btbuckets public views

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
            return self.response.write('')

        status = memcache.get(site) or counter.Counter()
        status.incr(uid)
        memcache.set(site, status)
        return self.response.out.write('__callback({"online": %s});' % 
                status.count())
