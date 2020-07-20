"""
Just some example tests and responses printed to console
"""
import CB.market
from datetime import datetime, timedelta

TICKER = 'BTC-USD'

# Get some general data
btc_ticker = CB.market.get_ticker(TICKER)
print(f'BTC-usd ticker info\n{btc_ticker}')

# historical data in 2d array format (from now to 5 days ago)
end = datetime.now()
start = end - timedelta(days=50)
granularity = 86400 # one-day candles
# Make sure to use iso format for date inputs
x = CB.market.get_forecastable_data(TICKER, start.isoformat(), end.isoformat(), granularity)
print(x)


# todo: example to make trade
