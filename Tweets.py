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

    def Past10(self, hashtag, amount, sincedate, untildate):
        if (sincedate==None or untildate ==None):
            today = datetime.datetime.now()
            limit = datetime.datetime(today.year,today.month,today.day-10)
            self.Past10(hashtag,today,limit,amount)
        day = sincedate
        print(day)
        nextday= day + datetime.timedelta(days=1)
        A = []
        twt = self.api.search(q=hashtag, count=amount, since= day,until= day, tweet_mode='extended', lang='en')
        for st in twt:
            A.append(st.full_text)
        if (day == untildate):
            return A
        if (day != untildate):
            A = A + self.Past10(hashtag,amount,nextday,untildate)





# startDate = datetime.datetime(2020, 7, 1, 0, 0, 0)
# endDate = datetime.datetime(2020, 1, 1, 0, 0, 0)
rt = Tweets()

a = rt.Past10('#Bitcoin',1,None,None)
print(a)

