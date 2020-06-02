import tweepy
import pandas as pd
from textblob import TextBlob
from config import keys as k

class Tweets():

    def __init__(self,keys):
        auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        self.api = tweepy.API(auth)

    def HashTweet(self, hashtag, amount):
        A = []
        if (lowid != None):  # if you dont have a previous itt,
            twt = self.api.search(q=hash, count=100)
            for st in twt:
                A.append(st.text)

        return (A)        