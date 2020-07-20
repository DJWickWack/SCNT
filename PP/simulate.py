import PP.forecast as forecast
from datetime import datetime
import CB.market
import pandas


'''
Lets do several forecasts to see what results we get.
Just a basic simulation to see how accurate simple momentum indication is.
'''

# Get hourly candles for the last month
start = datetime(2020, 6, 1, hour=20)
end = datetime(2020, 6, 18, hour=20)
granularity = 86400  #1-hour in seconds


csv_data = CB.market.historical_data_csv('BTC-USD', start, end, granularity)
forecast.ta_only_forecastMomentum(csv_data)