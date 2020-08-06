# Your project name

Trading cryptocurrency is a risky and difficult process. There are many factors that could affect the price of a digital asset with none of the protections that comes with US stock trading. In our project, we aim to determine the effects of public sentiment on the price of Bitcoin in order to create the foundation to a more accurate trading method which considers both sentiment-based and trend-based prediction models.

## Introduction

####Sentiment Analysis
For the sentiment analysis we use the textblob module: https://pypi.org/project/textblob

We gather information using a few sources:
* Twitter API - https://developer.twitter.com/en
* Feedparser for RSS feeds - https://pypi.org/project/feedparser/
* RapidAPI Contextual Web Search - https://rapidapi.com/contextualwebsearch/api/Web%20Search

Using these tools we can gather information about a specific cryptocurrency and input that data into textblob for an overall public sentimet/opinion.

####Technical Analysis
For the technical analysus, we used the pandas and TA libraries to perform analysus on Bitcoin specifically, however this can be applied to any cryptocurrency as is our plan in the future.
* Pandas - https://pypi.org/project/pandas/
* TA - https://pypi.org/project/ta/

We use the Coinbase API to gather historical price data, however this has some odd limitations and we plan on moving to something more versatile in the future.
We will also be using this API to perform automated trading once we are more satisfied with the progress we have made on our trading models.
* https://docs.pro.coinbase.com/

####Trading Methods
We combine a Stochastic Oscillator, Relative Strength Index, and our own Sentiment Analysis together to get an overall 
trading decision based on what each of these say. A Stochastic Oscillator and Relative Strength Index are very sensitive
trading models that can have many false positives.

Using these models with high volatility allow us to determine whether applying decisions based on Sentiment Analysis 
actually made a difference, or if we need to tweak our models to avoid the false positives/negatives. 

More info on trading methods:
* Stocastic Oscillator - https://www.investopedia.com/terms/s/stochasticoscillator.asp
* Relative Strength Index - https://www.investopedia.com/terms/r/rsi.asp

## Features
1. Gather price data from Coinbase
2. Get data in JSON, CSV, and Dictionary formats
3. Gather news related to any topic, and from any time
4. Gather tweets related to any topic, and any time up to a week ago
5. Gather articles from RSS feeds
6. With data ranging more than 14 entries, use TA to get price velocity

## Getting Started
### Usage
Currently the project is in a POC stage, where we are exploring the best ways to predict Bitcoin price using Sentiment and moderately volatile TA methods. Because of this, our project
is mainly a collection of python modules that can be imported into your own project should you decide to use them.

Once you have imported them into your project, there are a few API credentials that must be added:
* CB
    * Under auth.py, add API_SECRET, API_PASS, API_KEY credentials.
* News
    * In search.py, add RapidAPI credentials in both headers variables for NewsSearch and NewsDaySearch
* Config.py
    * add consumer_key, consumer_secret, access_token, and access_token_secret from Twitter API


## Demo video
https://www.youtube.com/watch?v=iPPa9Q0pQo0

## Contributors

* Bruce Craig, Social API's and Sentiment Analysis
* Alan Smith, Coinbase/News API's and Technical Analysis

