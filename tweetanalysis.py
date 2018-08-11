import tweepy
from constants import *
import numpy as np
import csv
from textblob import TextBlob
import matplotlib.pyplot as plt



#Get user id
username = input("What is username? ")

#Authentication using API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Create array of all tweets and retweets
def get_Tweets(username):
    global alltweets
    global retweets
    global all_no_rts
    global allstatuses
    alltweets = []
    retweets = []
    all_no_rts = []
    allstatuses = []
    for status in tweepy.Cursor(api.user_timeline, screen_name=username, count=200).items():
        alltweets.append(status._json['text'])
        allstatuses.append(status)
    for tweet in alltweets:
        if (tweet[:2] != "RT"):
            all_no_rts.append(tweet)
        else:
            retweets.append(tweet)
    print(len(alltweets))

def get_Date(status):
    date = status._json["created_at"]
    month = date[4:7]
    year = date[-4:]
    return [month,year]

def find_sentiment(tweets_list):
    global positive_num
    positive_num= 0
    global negative_num
    negative_num = 0
    total_polarity_all = 0
    total_subj_all = 0
    global neutral_num
    neutral_num = 0
    global polarity
    global subjectivity
    for tweet in tweets_list:
        text = TextBlob(tweet)
        total_polarity_all += text.sentiment.polarity
        total_subj_all += text.sentiment.subjectivity
        if (text.sentiment.polarity > 0):
            positive_num += 1
        elif (text.sentiment.polarity < 0) :
            negative_num += 1
        else:
            neutral_num += 1
    polarity = total_polarity_all / len(tweets_list)
    subjectivity = total_subj_all / len(tweets_list)
    return polarity

def sort_Time_graph(status_list):
    sorted_statues= []
    tweet_groups = []
    group_number = []
    for status in status_list:
        date = get_Date(status)
        month = date[0]
        year = date[1]
        if len(sorted_statues) == 0:
            sorted_statues.append([status])
        if len(sorted_statues) != 0:
            last_array = sorted_statues[-1]
            last_date = get_Date(last_array[0])
            if month == last_date[0] and year == last_date[1]:
                last_array.append(status)
            else:
                sorted_statues.append([status])
    for list in sorted_statues:
        tweet_groups.append(get_Date(list[0]))
        group_number.append(len(list))

    #Create bar graph
    y_pos = np.arange(len(tweet_groups))
    plt.bar(y_pos, group_number, align='center', alpha=0.5)
    plt.xticks(y_pos, tweet_groups)
    plt.ylabel('Number of Tweets')
    plt.title("Number of tweets a month")
    print("Graph working")
    plt.show()


#Sentiment Analysis
def find_sentiment_graph(tweets_list):
    global positive_num
    positive_num= 0
    global negative_num
    negative_num = 0
    total_polarity_all = 0
    total_subj_all = 0
    global neutral_num
    neutral_num = 0
    global polarity
    global subjectivity
    for tweet in tweets_list:
        text = TextBlob(tweet)
        total_polarity_all += text.sentiment.polarity
        total_subj_all += text.sentiment.subjectivity
        if (text.sentiment.polarity > 0):
            positive_num += 1
        elif (text.sentiment.polarity < 0) :
            negative_num += 1
        else:
            neutral_num += 1
    polarity = total_polarity_all / len(tweets_list)
    subjectivity = total_subj_all / len(tweets_list)
    print("Average Polarity: " + str(polarity))
    print("Average Subjectivity: " + str(subjectivity))

    #Graph pie chart: positive and negative
    labels = 'Positive', 'Negative', "Neutral"
    percentages = [positive_num / len(tweets_list), negative_num / len(tweets_list), neutral_num/ len(tweets_list)]
    fig1, ax1 = plt.subplots()
    ax1.pie(percentages, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

    #Graph bar graphL
get_Tweets(username)
sort_Time_graph(allstatuses)









