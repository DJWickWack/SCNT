import PP.forecast as forecast
from datetime import datetime

# last 4 months of dates
dates = [
    datetime(2020, 4, 12, hour=20),
    datetime(2020, 5, 12, hour=20),
    datetime(2020, 6, 12, hour=20),
    datetime(2020, 6, 23, hour=20),
    datetime(2020, 7, 12, hour=20),
]

# lets forecast BTC for those dates
for d in dates:
    f = forecast.forecastMomentum('BTC-USD', d)
    if f == 1:
        print(f'{d} Should hold asset')
    elif f == 2:
        print(f'{d} price will go down')
    elif f == 0:
        print(f'{d} price will go up')
