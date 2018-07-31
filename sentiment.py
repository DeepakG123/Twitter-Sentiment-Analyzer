from textblob import TextBlob
import csv

alltweets = []


text = TextBlob("We must have Border Security, get rid of Chain, Lottery, Catch & Release Sanctuary Cities - go to Merit based Immigration. Protect ICE and Law Enforcement and, of course, keep building, but much faster, THE WALL!")
print(text.sentiment)