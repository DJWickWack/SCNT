import PP.forecast as forecast
from datetime import datetime
import CB.market

# last 4 months of dates
start = datetime(2020, 7, 1, hour=12)

end = datetime(2020, 7, 18, hour=0)

x = CB.market.historical_data_csv('BTC-USD', start, end, 3600)
