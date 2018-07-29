import tweepy
from constants import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

users = ['xoroohi', 'ruchikakkad04','DeepakG_1234']

alltweets = []

tweets = api.user_timeline(screenname = 'ruchikakkad04', count = 200)

alltweets.extend(tweets)

oldest = alltweets[-1].id - 1

while len(tweets) > 0:
    print("getting tweets before %s" % (oldest))
    new_tweets = api.user_timeline(screen_name= 'ruchikakkad04', count=200, max_id=oldest)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    print("...%s tweets downloaded so far" % (len(alltweets)))
