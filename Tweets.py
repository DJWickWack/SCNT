import tweepy
import pandas as pd
from config import key as key

class Tweets():

    def __init__(self):
        auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
        auth.set_access_token(key.access_token, key.access_token_secret)
        self.api = tweepy.API(auth)

    def HashTweet(self, hashtag, amount,lowid):
        A = []
        if (lowid != None):  # if you dont have a previous itt,
            twt = self.api.search(q=hashtag, count=amount, tweet_mode='extended', max_id=lowid, lang='en')
            for st in twt:
                A.append(st)
        else:
            twt = self.api.search(q=hashtag, count=amount, tweet_mode='extended', lang='en')
            for st in twt:
                A.append(st.full_text)
        return A
#for testing
# rt = Tweets()
# a = rt.HashTweet('#Bitcoin',10,None)
# print(a)

