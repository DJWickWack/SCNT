"""
For now, lets just work with the BTC-USD ticker and expand from there once main functionality works
"""
import CB.auth
import requests
import json

"""
# Gets raw ticker data and returns json
# Example
 {
     "trade_id": 13786402,
     "price": "8966.22",
     "size": "0.0861",
     "time": "2020-06-15T06:46:37.645775Z",
     "bid": "8966.22",
     "ask": "8966.24",
     "volume": "2122849.93895368"
 }
"""
def get_ticker(id):
    info = json.loads(requests.get(CB.auth.api_url + f'products/{id}/ticker').content)  # no auth necessary
    return info

"""
# Get price based on some time
# Coinbase returns a 2d list like this:
[
    [ 1415398768, 0.32, 4.2, 0.35, 4.2, 12.3 ],
    [ 1415398948, 0.77, 4.4, 0.36, 4.2, 8.8 ],
    ...
]

# each entry is in the form:
    [ time, low, high, open, close, volume ]

granularity field must be one of the following values: {60, 300, 900, 3600, 21600, 86400}
    essentially length of candle time in seconds
time inputs must be ISO 8601 (YYYY-MM-DD)

:var id - some ticker id like 'BTC-USD'
:var start - some ISO8601 starting time
:var end - some ISO8601 ending time 
:return hashmap in the form: {unix_timestamp:{datatype:data}} where datatype is time, low, high, etc.. like above
"""
def historical_data_hashtable(id, start, end, granularity):

    params = {
        'start': start,
        'end': end,
        'granularity': granularity
    }
    try:
        response = requests.get(CB.auth.api_url + f'products/{id}/candles', params=params)  # no auth necessary
        json_data = response.json()

        # parse json to hashtable
        historical_data_hashtable = {}
        for entry in json_data:
            entry_map = {
                'time':entry[0],
                'low':entry[1],
                'high':entry[2],
                'open':entry[3],
                'close':entry[4],
                'volume':entry[5]
            }
            historical_data_hashtable[entry_map['time']] = entry_map

        return historical_data_hashtable

    except Exception as error:
        print('ERROR Getting Historic Data\n')
        print(error)

"""
# Get price based on some time
# Coinbase returns a 2d list like this:
[
    [ 1415398768, 0.32, 4.2, 0.35, 4.2, 12.3 ],
    [ 1415398948, 0.77, 4.4, 0.36, 4.2, 8.8 ],
    ...
]

granularity field must be one of the following values: {60, 300, 900, 3600, 21600, 86400}
    essentially length of candle time in seconds
time inputs must be ISO 8601 (YYYY-MM-DD)

:var id - some ticker id like 'BTC-USD'
:var start - some ISO8601 starting time
:var end - some ISO8601 ending time 
:return raw json response - 2d array of data like above. Useful for TA
"""
def historical_data_json(id, start, end, granularity):

    params = {
        'start': start,
        'end': end,
        'granularity': granularity
    }
    try:
        response = requests.get(CB.auth.api_url + f'products/{id}/candles', params=params)  # no auth necessary
        json_data = response.json()

        return json_data

    except Exception as error:
        print('ERROR Getting Historic Data\n')
        print(error)


