import PP.forecast as forecast
from datetime import datetime
import CB.market
import pandas

# Get hourly candles for the last month
start = datetime(2020, 6, 19, hour=20)
end = datetime(2020, 7, 1, hour=20)
granularity = 3600  #1-hour in seconds

csv_data = CB.market.historical_data_csv('BTC-USD', start, end, granularity)

forecast.forecastMomentum(csv_data)
