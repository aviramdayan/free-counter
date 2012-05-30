Really simple online visitors counter using google appengine's memcache.
It was build to use with "SiteApps.com - http://siteapps.com/app/online_visitor_counter-238"

Search for the app "Online Visitor Counter"

It uses an uniq ID to identify users on a dict and expire the visit after a pre-configured time.

It should run in conjunction a simple java script that need to care about:

-An uniq ID to the visitor
-An uniq ID for the website
-Set the cookie with the uniq visitor's ID
-A function to show the online counter
