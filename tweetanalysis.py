import tweepy
from constants import *
import csv
from textblob import TextBlob


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
for status in tweepy.Cursor(api.user_timeline, screen_name='xoroohi').items():
    number_tweets = number_tweets  + 1
    alltweets.append(status._json['text'])
print(number_tweets)

#Populate all_no_rts
for tweet in alltweets:
    if(tweet[:2] !=  "RT"):
        all_no_rts.append(tweet)

#Sentiment Analysis
total_polarity = 0;
total_subj = 0;
for tweet in all_no_rts:
    text = TextBlob(tweet)
    total_polarity += text.sentiment.polarity
    total_subj += text.sentiment.subjectivity
polarity = total_polarity/len(alltweets)
subjectivity = total_subj/len(alltweets)

print(len(all_no_rts))

print("Average Polarity: " + str(polarity))
print("Average Subjectivity: " + str(subjectivity))

# #Save to CSV file
# with open('tweets.csv', 'w+') as new_file:
#     csv_writer = csv.writer(new_file, delimiter = "-")
#
#     for tweet in alltweets:
#         row = [tweet.encode('utf-8')]
#         csv_writer.writerow([tweet])





