import datetime

import tweepy
import pandas as pd
from config import key as key

class Tweets():

    def __init__(self):
        auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
        auth.set_access_token(key.access_token, key.access_token_secret)
        self.api = tweepy.API(auth)

    def HashTweet(self, hashtag, amount):
        A = []
        twt = self.api.search(q=hashtag, count=amount, tweet_mode='extended', lang='en')
        for st in twt:
            A.append(st.full_text)
        return A

    def Past10(self, hashtag, amount):


        limit = datetime.datetime.now() - datetime.timedelta(days=7)
        A = []
        for x in range(8):
            twt = self.api.search(q=hashtag, count=amount, until= limit.isoformat(), tweet_mode='extended', lang='en')
            for y in twt:
                A.append(y.full_text)
            limit += datetime.timedelta(days=1)

        return A

    def getDay(self, hashtag, amount, day):


        limit = datetime.datetime.now() - datetime.timedelta(days=7)
        if (day<limit):
            raise ValueError('day is less than the limit of 7 days in the past')
        A = []

        twt = self.api.search(q=hashtag, count=amount, until= day.isoformat(), tweet_mode='extended', lang='en')
        for y in twt:
            A.append(y.full_text)


        return A







