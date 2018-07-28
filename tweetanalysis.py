import tweepy
from constants import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_me = api.get_user('DeepakG_1234')
user_roohi = api.get_user('xoroohi')
user_ruchi = api.get_user('ruchikakkad04')
user_god = api.get_user('CaseyNeistat')

users = [user_me, user_roohi, user_ruchi, user_god]

for user in users:
    print("-------------------")
    print('Name: ' + user.name)
    print('Location: ' + user.location)
    print('Friends: ' + str(user.friends_count))


for status in tweepy.Cursor(api.user_timeline).items():
    print(status.text)