import datetime as datetime

from RSSFeeds import RSSFeeds
from Tweets import Tweets
import CB.market
import News.search as search
from datetime import datetime, timedelta
from SentAnalysis import SentAnalysis

rss = RSSFeeds()
print('\n====RSS Feeds====')

feed = rss.GetFeed('https://cointelegraph.com/rss/tag/bitcoin')
for x in rss.GetArticles(feed):
    print(x['title'])

tw = Tweets()
print('\n====10 recent Tweets that have #Bitcoin====')
listoftweets = tw.HashTweet('#Bitcoin',10,None)
print(listoftweets)


sa=SentAnalysis()
print('\n====Sent Analysis of every article====')
print(sa.rssAnalysis(rss.GetArticles(feed)))
print('\n====Sent Analysis of every tweet====')
print(sa.tweetAnalysis(listoftweets))
print('\n====Total Avg of both====')
print(sa.getAnalysis(listoftweets,rss.GetArticles(feed)))



TICKER = 'BTC-USD'
# Get some general data
btc_ticker = CB.market.get_ticker(TICKER)
print(f'\n====BTC-usd ticker info====\n{btc_ticker}\n\n')

# historical data in 2d array format (from now to 5 days ago)
end = datetime.now()
start = end - timedelta(days=20)
granularity = 86400 # one-day candles
# Make sure to use iso format for date inputs
x = CB.market.historical_data_json(TICKER, start.isoformat(), end.isoformat(), 86400)
print("====Last Month of Daily Candles====\n[time, low, high, open, close, volume]")
for entry in x:
    print(entry)

print("\n====Historical prices====")
list = []
for entry in x:
    list.append(entry[4])
print(list)

#gets a bunch of recent articles on bitcoin
print("\n\n====Recent News Article Mentioning Bitcoin====")
news = search.NewsSearch('bitcoin')
for i in range(1):
    print(f'TITLE: {news["value"][i]["title"]}')
    print(f'BODY:\n{news["value"][i]["body"]}\n')