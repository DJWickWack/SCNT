import PP.forecast as forecast
from datetime import datetime, timedelta
import CB.market
import pandas


'''
Lets do several forecasts to see what results we get.
Just a basic simulation to see how accurate simple momentum indication is.
'''

# Get hourly candles for the last month
time = datetime.now()
granularity = 86400  #1-hour in seconds
csv_data = CB.market.get_forecastable_data('BTC-USD', time, granularity)
forecast.ta_only_forecastMomentum(csv_data)

