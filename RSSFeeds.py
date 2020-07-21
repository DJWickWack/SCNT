import feedparser
import bs4

class RSSFeeds():

    def GetFeed(self, feedurl):
        return feedparser.parse(feedurl)

    '''
    Input: Parsed RSS feed
    Output: List of articles. Each article is a dictoinary containing the following data:
        'id': url to article
        'title': title of article
        'summary': summary of article
        'date': date article published
        'texts': all strings of text found inside <p></p>
        
    '''
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

        # Add entry to articles, contains list of paragraph texts to analyze
        # todo: generating duplicates for me, but works for now.
        for article in arts:
            soup = bs4.BeautifulSoup(article['summary'], features="html.parser")
            paragraphs = soup.find_all('p')
            text_found = []
            for p in paragraphs:
                text_found.append(p.text)
            article['texts'] = text_found

        return arts
    def SaveTexts (self,arts,filename):
        file=open(filename,"w")
        for x in arts:
            file.write((x['texts'][0]+" \n"))
        file.close()
        print("File saved!")

    def LoadTexts (self,filename):
        file = open(filename,"r")
        temp = file.readlines()
        for x in temp:
            x.replace(" \n", "")
        return temp




# for testing
# d = RSSFeeds()
# f = d.GetFeed('https://cointelegraph.com/rss/tag/bitcoin')
# d.SaveTexts(d.GetArticles(f),"DemoTexts.txt")
# for x in d.LoadTexts("DemoTexts.txt"):
#     print(x)

