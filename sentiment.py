from textblob import TextBlob
import csv

alltweets = []


text = TextBlob("everyone is fucking leaving all the time")
print(text.sentiment)