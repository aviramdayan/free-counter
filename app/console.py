#!/usr/bin/python
import code
import getpass
import sys
import os
sys.path.append("/usr/local/google_appengine")

DIR_PATH = '/usr/local/google_appengine'
EXTRA_PATHS = [
  DIR_PATH,
  os.path.join(DIR_PATH, 'lib', 'antlr3'),
  os.path.join(DIR_PATH, 'lib', 'django'),
  os.path.join(DIR_PATH, 'lib', 'ipaddr'),
  os.path.join(DIR_PATH, 'lib', 'webob'),
  os.path.join(DIR_PATH, 'lib', 'yaml', 'lib'),
  os.path.join(DIR_PATH, 'lib', 'fancy_urllib'),
]

sys.path = EXTRA_PATHS + sys.path


from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db

def auth_func():
  return raw_input('Username:'), getpass.getpass('Password:')

if len(sys.argv) < 2:
  print "Usage: %s app_id [host]" % (sys.argv[0],)
app_id = sys.argv[1]
if len(sys.argv) > 2:
  host = sys.argv[2]
else:
  host = '%s.appspot.com' % app_id.replace('s~', '')

remote_api_stub.ConfigureRemoteDatastore(app_id, '/_ah/remote_api', auth_func, host)

code.interact('App Engine interactive console for %s' % (app_id,), None, locals())
