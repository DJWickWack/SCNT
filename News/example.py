import datetime

import News.search as search

#gets a bunch of recent articles on bitcoin
news = search.NewsSearch('bitcoin')
timednews=search.NewsDaySearch('bitcoin',datetime.datetime(2020, 7, 24, 0, 0, 0),datetime.timedelta(days=1))
for article in news['value']:
    print(f'TITLE: {article["title"]}')
    print(f'Date:\n{article["datePublished"]}\n')

for article in timednews['value']:
    print(f'TITLE: {article["title"]}')
    print(f'Date:\n{article["datePublished"]}\n')
