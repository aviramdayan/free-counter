#!/usr/bin/env python                                                                                                                                      
# coding: utf-8
 
import logging
 
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
 
from graphssss import views
 
# uri mapping - pascal triangle.
urls = (
  (r'/graphssss/slogs/', views.SaveLog),
  (r'/graphssss/glogs/', views.GetLog),
)
 
def main():
  app = webapp.WSGIApplication(urls, debug=False)
  util.run_wsgi_app(app)
 
if __name__ == '__main__':
  log = logging.getLogger()
  log.setLevel(logging.ERROR)
  main()
