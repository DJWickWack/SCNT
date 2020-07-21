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

    def HashTweet(self, hashtag, sincedate, untildate, amount):
        A = []
        twt = self.api.search(q=hashtag, count=100, since= sincedate,until= untildate, tweet_mode='extended', lang='en')
        for st in twt:

            A.append(st.full_text)

        return A



startDate = datetime.datetime(2020, 7, 1, 0, 0, 0)
endDate = datetime.datetime(2020, 1, 1, 0, 0, 0)
rt = Tweets()
datee = (startDate, endDate)
a = rt.HashTweet('#Bitcoin',datee,10,None)
print(a)

