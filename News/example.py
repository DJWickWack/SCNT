import News.search as search

#gets a bunch of recent articles on bitcoin
news = search.NewsSearch('bitcoin')
for article in news['value']:
    print(f'TITLE: {article["title"]}')
    print(f'BODY:\n{article["body"]}\n')
