import os
import sys
import tweepy
import datetime
import ConfigParser


class StdOutListener(tweepy.StreamListener):
	def on_status(self, status):
		# Prints the streaming tweets
		print('Tweet text: ' + status.text).encode('utf8')
	'''
		for hashtag in status.entries['hashtags']:
			print(hashtag['text'])
		return True
	'''
	def on_error(self, status_code):
		print('Got an error with status code: ' + str(status_code))
		return True # To continue listening
	
	def on_timeout(self):
		print('Timeout...')
		return True # To continue listening
 
def settings_check():
	try:
		
		config = ConfigParser.ConfigParser()
		config.read(settings_ini)
		
		cust_key = config.get('credentials', 'consumer_key').strip()
		cust_sec_key = config.get('credentials', 'consumer_secret_key').strip()
		acc_key = config.get('credentials', 'access_token').strip()
		acc_sec_key = config.get('credentials', 'access_secret_token').strip()
		user1 = config.get('tweeterats', 'user1').strip()
		return cust_key, cust_sec_key, acc_key, acc_sec_key, user1
	
	except Exception, e:
		print str(e)


if __name__ == '__main__':

	listener = StdOutListener()
	
	# Set date time stamp for log file
	date_stamp = datetime.datetime.now().strftime("%Y_%m_%d_%H%M")
	# We set the home dir for the scanner here 
	home_dir = os.getcwd()
	# The INI containing settings should be in the home directory
	settings_ini = home_dir+"\\tweet.ini"
	# Read settings.ini for various settings
	settings = settings_check()
	CONSUMER_KEY = settings[0]
	CONSUMER_SECRET = settings[1]
	OAUTH_TOKEN = settings[2]
	OAUTH_SECRET = settings[3]
	follower1 = settings[4]
	
	# Continue our script only if we find the basic values
	if CONSUMER_KEY != '' and CONSUMER_SECRET != '' and OAUTH_TOKEN != '' and OAUTH_SECRET != '' and follower1 != '':
		print follower1
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
		track = [follower1]
		stream = tweepy.Stream(auth, listener)
		stream.filter(track=track)
