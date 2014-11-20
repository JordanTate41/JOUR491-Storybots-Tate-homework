from bs4 import BeautifulSoup

from twython import Twython

import urllib, urllib2, string, datetime, time, re, random

API_KEY = 
API_SECRET = 
ACCESS_TOKEN = 
ACCESS_TOKEN_SECRET = 

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

homerquotes = []

f = open('homersimpson2.db', 'r')

for line in f:
	if len(line) != 1:
		if len(line)<140:
		    homerquotes.append(line)
		else:
		    pass
	else:
		pass
		
search_results = twitter.search(q='#HomerSimpson', count=5)
print search_results

for tweet in search_results['statuses']:
	try: 
	    tweetthis = "@%s %s" % (tweet['user']['screen_name'].encode('utf-8'), random.choice(homerquotes))
	    twitter.update_status(status=tweetthis, in_reply_to_status_id=tweet['id'])
	except:
		 continue