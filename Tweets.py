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


        limit = datetime.datetime.now() - datetime.timedelta(days=10)
        A = []
        for x in range(10):
            twt = self.api.search(q=hashtag, count=amount, since=limit, until=limit, tweet_mode='extended', lang='en')
            for y in twt:
                A.append(y.full_text)
            limit += datetime.timedelta(days=1)

        return A






# startDate = datetime.datetime(2020, 7, 1, 0, 0, 0)
# endDate = datetime.datetime(2020, 1, 1, 0, 0, 0)
rt = Tweets()
a= rt.HashTweet("#bitcoin",10)
# a = rt.Past10('#Bitcoin',1)
print(a)

