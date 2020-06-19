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
start = end - timedelta(days=5)
granularity = 86400 # one-day candles
# Make sure to use iso format for date inputs
x = CB.market.historical_data_json(TICKER, start.isoformat(), end.isoformat(), 86400)
print("[time, low, high, open, close, volume]")
for entry in x:
    print(entry)

# todo: might be helpful to convert historical data to csv for TA library

# todo: example to make trade
