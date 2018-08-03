import tweepy
from constants import *
from tweetanalysis import get_Tweets
from tweetanalysis import find_sentiment

#Authentication using API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
