#!/usr/bin/env python
# coding: utf-8

import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import views

# uri mapping - pascal triangle.
urls = (
  (r'/get/', views.Get),
)

def main():
  app = webapp.WSGIApplication(urls, debug=False)
  util.run_wsgi_app(app)

if __name__ == '__main__':
  log = logging.getLogger()
  log.setLevel(logging.ERROR)
  main()
