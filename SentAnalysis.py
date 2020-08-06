import datetime

from textblob import TextBlob
from Tweets import Tweets
from RSSFeeds import RSSFeeds
import News.search as search


class SentAnalysis():
    def get7dayAnalysis(self, topic):
        # This takes in both a list of tweet text and an arr of rss feed news
        # This will return a single number based off all the returning analysis
        news = search.NewsSearch(topic)
        d = RSSFeeds()
        tw = Tweets()
        tweets = tw.Past10('#'+topic, 10)
        f = d.GetFeed('https://cointelegraph.com/rss/tag/'+topic)
        rss= d.GetArticles(f)
        total_anal = self.tweetAnalysis(tweets) + self.rssAnalysis(rss)+self.newsAnalysis(news)
        res = 0
        for x in total_anal:
            res += x
        return res/len(total_anal)

    def getdayAnalysis(self, topic, day):
        # This takes in both a list of tweet text and an arr of rss feed news
        # This will return a single number based off all the returning analysis
        news = search.NewsDaySearch(topic,day,datetime.timedelta(days=1))
        d = RSSFeeds()
        tw = Tweets()
        tweets = tw.getDay('#'+topic, 10, day)
        f = d.GetFeed('https://cointelegraph.com/rss/tag/'+topic)
        rss= d.GetArticles(f)
        total_anal = self.tweetAnalysis(tweets) + self.rssAnalysis(rss)+self.newsAnalysis(news)
        res = 0
        for x in total_anal:
            res += x
        return res/len(total_anal)


    def tweetAnalysis(self,tweets):
        tweetsent=[]
        for tx in tweets:
            blob = TextBlob(tx)
            tweetsent.append(blob)
        for x in range(0,(len(tweetsent))):
            tweetsent[x]=tweetsent[x].sentiment.polarity
        return tweetsent

    def rssAnalysis(self,news):
        newssent=[]
        for nw in news:
            blob=TextBlob(nw['texts'][0])
            newssent.append(blob)
        for x in range(0, (len(newssent))):
            newssent[x] = newssent[x].sentiment.polarity
        return newssent

    def newsAnalysis(self,news):
        newsbody=[]
        newstitle=[]
        for article in news['value']:
            blob = TextBlob(article["body"])
            newsbody.append(blob.sentiment.polarity)
        for article in news['value']:
            blob = TextBlob(article["title"])
            newstitle.append(blob.sentiment.polarity)
        return newsbody+newstitle
