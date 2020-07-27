'''
Small script to grab some news data about some currency and respond with the json RSS data
'''

import requests

def NewsSearch(query):
    # base parameters for query
    querystring = {
        "autoCorrect": "false",
        "pageNumber": "1",
        "pageSize": "50",
        "safeSearch": "false",
        'q': query
    }

    # API keys should be obfuscated/secured somehow for a Non-POC
    # I am 'paying' for this api key but my virtual card has a $1 limit. it should stay free for the
    #   first 10000 searches though
    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "948fe9c868msh9cf61cb73a42fddp176157jsn14144f040a4a"
    }
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"
    response = requests.request("GET", url, headers=headers, params=querystring)
    json = response.json()

    #  todo: maybe i shouldn't leave the responsibility of parsing to something higher in the stack
    return json

def NewsDaySearch(query,date,delta):
    # base parameters for query
    fromdate = date - delta
    querystring = {
        "fromPublishedDate": fromdate.isoformat(),
        "toPublishedDate": date.isoformat(),
        "autoCorrect": "false",
        "pageNumber": "1",
        "pageSize": "50",
        "safeSearch": "false",
        'q': query
    }

    # API keys should be obfuscated/secured somehow for a Non-POC
    # I am 'paying' for this api key but my virtual card has a $1 limit. it should stay free for the
    #   first 10000 searches though
    headers = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "948fe9c868msh9cf61cb73a42fddp176157jsn14144f040a4a"
    }
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"
    response = requests.request("GET", url, headers=headers, params=querystring)
    json = response.json()

    #  todo: maybe i shouldn't leave the responsibility of parsing to something higher in the stack
    return json
