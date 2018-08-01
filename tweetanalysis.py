import tweepy
from constants import *
import csv
from textblob import TextBlob
import matplotlib.pyplot as plt



#Get user id
username = input("What is username? ")

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
for status in tweepy.Cursor(api.user_timeline, screen_name= username, count =200).items():
    number_tweets = number_tweets  + 1
    alltweets.append(status._json['text'])
print(number_tweets)

#Populate all_no_rts and retweets
for tweet in alltweets:
    if(tweet[:2] !=  "RT"):
        all_no_rts.append(tweet)
    else:
        retweets.append(tweet)

# #Sentiment Analysis
# def find_sentiment(username):
#


#All tweets
positive_num = 0
negative_num = 0
total_polarity_all = 0
total_subj_all = 0;
for tweet in all_no_rts:
    text = TextBlob(tweet)
    total_polarity_all += text.sentiment.polarity
    total_subj_all += text.sentiment.subjectivity
    if(text.sentiment.polarity > 0):
        positive_num += 1
    else:
        negative_num += 1
polarity = total_polarity_all /len(all_no_rts)
subjectivity = total_subj_all/len(all_no_rts)

print(len(all_no_rts))

print("Average Polarity: " + str(polarity))
print("Average Subjectivity: " + str(subjectivity))

#Data Visualization
labels = 'Positive', 'Negative'
percentages = [positive_num /len(all_no_rts), negative_num /len(all_no_rts)]
fig1, ax1 = plt.subplots()
ax1.pie(percentages,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
# #Save to CSV file
# with open('tweets.csv', 'w+') as new_file:
#     csv_writer = csv.writer(new_file, delimiter = "-")
#
#     for tweet in alltweets:
#         row = [tweet.encode('utf-8')]
#         csv_writer.writerow([tweet])





