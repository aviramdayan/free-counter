# encoding: utf-8

import logging

from time import time

from google.appengine.api.logservice import logservice
from google.appengine.ext import webapp, db
from django.utils import simplejson as json


from graphssss.models import Log
from graphssss import settings

class SaveLog(webapp.RequestHandler):
    def get(self):
        end_time = time()
        #TODO: start_time must be on settings file
        start_time = end_time - settings['TIME_TO_FETCH']
        data=[]

        #Avoind the dots for performance
        record_graphssss_req=settings['RECORD_GRAPHSSSS_REQ']
        graphssss_resource=settings['RESOURCE']

        for req_log in logservice.fetch(start_time=start_time, end_time=end_time, offset=None,
                      minimum_log_level=logservice.LOG_LEVEL_INFO,
                      include_app_logs=False):
            if req_log.resoruce.startswith(graphssss_resource) and not record_graphssss:
                continue
            data.append(dict(
                    cost=req_log.cost,
                    mcycles=req_log.mcycles,
                    latency=req_log.latency,
                    pending=req_log.pending_time,
                    size=req_log.response_size,
                    loading_request=req_log.was_loading_request,
                    time=req_log.start_time,
                    #resorce=req_log.resource
                    ))
        if not data:
            logging.info('GRAPHSSSS: There is no logs to record on DS')
            return self.response.out.write('nothing to save')

        log=Log(data=json.dumps(data))
        log.save()
        self.response.out.write('saved')

class GetLog(webapp.RequestHandler):
    def get(self):
        remove_key=self.request.get('_rkey')
        if remove_key:
            db.delete(remove_key)
            return self.response.out.write('key: %s removed' % remove_key)

        log=Log.all().order('date').fetch(1)
        try:
            log=log[0]
        except IndexError:
            logging.info('GRAPHSSSS: there is no log to fetch from DS')
            return self.response.out.write('')
        data=json.loads(log.data)
        self.response.headers['X-GRA_KEY']=str(log.key())
        return self.response.out.write(json.dumps(data))
