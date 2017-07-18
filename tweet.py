import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

latesttweet = open('latesttweet.txt', 'r') 
trumptweet = latesttweet.read()
latesttweet.close 



stuff = api.user_timeline(screen_name = 'realDonaldTrump', count = 1, include_rts = False)   
 
for status in stuff:
	tweet = status.text 
	id = status.id

if trumptweet != tweet:
	api.update_status("Hello from the Trump Twitter bot. For all sake please stop tweeting", in_reply_to_status_id = id) 
	f = open('latesttweet.txt', 'w')
	f.write(tweet) 
	f.close 
	
	
if trumptweet == tweet:
	print "done" 

	




