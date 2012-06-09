from google.appengine.ext import db



class Log(db.Model):
    date=db.DateTimeProperty(indexed=True, auto_now=True)
    data=db.TextProperty()
