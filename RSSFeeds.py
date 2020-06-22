import feedparser
import bs4

class RSSFeeds():

    def GetFeed(self, feedurl):
        return feedparser.parse(feedurl)

    def GetArticles(self, feed):
        arts = []
        entries = feed['entries']
        for x in entries:
            arts.append({
                'id': x['id'],
                'title': x['title'],
                'summary': x['summary'],
                'date': x['published_parsed']
            })
        return arts


# for testing
d = RSSFeeds()
f = d.GetFeed('https://cointelegraph.com/rss/tag/bitcoin')
print(d.GetArticles(f)[0]['summary'])
