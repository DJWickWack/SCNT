import tweepy
import pandas as pd
from textblob import TextBlob
from config import keys as k

class Tweets():

    def __init__(self,keys):
        auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        self.api = tweepy.API(auth)

    def HashTweet(self, hashtag, amount,lowid):
        A = []
        if (lowid != None):  # if you dont have a previous itt,
            twt = self.api.search(q=hashtag, count=amount, tweet_mode='extended', max_id=lowid)
            for st in twt:
                A.append(st.name) #name is temp for testing purposes
        else:
            twt = self.api.search(q=hashtag, count=amount, tweet_mode='extended')
            for st in twt:
                A.append(st.name)  # name is temp for testing purposes
        print(A)
        return A




