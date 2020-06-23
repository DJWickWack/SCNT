from textblob import TextBlob
from Tweets import Tweets
from RSSFeeds import RSSFeeds


class SentAnalysis():
    def getAnalysis(self, tweets, news):
        # This takes in both a list of tweet text and an arr of rss feed news
        # This will return a single number based off all the returning analysis
        total_anal = self.tweetAnalysis(tweets) + self.rssAnalysis(news)
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
#for testings
sa=SentAnalysis()
tw=Tweets()
rs=RSSFeeds
d = RSSFeeds()
f = d.GetFeed('https://cointelegraph.com/rss/tag/bitcoin')
print(sa.rssAnalysis(d.GetArticles(f)))
print(sa.tweetAnalysis(tw.HashTweet('#bitcoin',10,None)))
print(sa.getAnalysis(tw.HashTweet('#bitcoin',10,None),d.GetArticles(f)))