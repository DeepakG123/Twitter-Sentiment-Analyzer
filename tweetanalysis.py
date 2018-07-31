import tweepy
from constants import *
import csv


#Authentication using API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#KList of test users
users = ['xoroohi', 'ruchikakkad04','DeepakG_1234']

#Array to store tweets
alltweets = []
retweets = []
all_no_rts = []


#Retrieves whole timeline
number_tweets = 0
for status in tweepy.Cursor(api.user_timeline, screen_name='ruchikakkad04').items():
    number_tweets = number_tweets  + 1
    alltweets.append(status._json['text'].encode('utf-8'))
print(number_tweets)
print((alltweets))

#Save to CSV file
with open('tweets.csv', 'w+') as new_file:
    csv_writer = csv.writer(new_file, delimiter = "-")

    for tweet in alltweets:
        csv_writer.writerow([tweet])





