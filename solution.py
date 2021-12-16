import requests
import json
import tweepy
from keys import api_key,bearer_Token,api_secret

def requestDataTwitter():
    auth = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret=api_secret)
    auth.set_access_token()
    api = tweepy.API(auth)

    cusor = tweepy.Cursor(api.user_timeline, id="Barack Obama", tweet_mode = "extended").items(1)

    for i in cusor:
        print(i)