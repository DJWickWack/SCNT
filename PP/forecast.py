import CB.market as market
from datetime import datetime, timedelta
import pandas
import os
from ta import momentum
import time

'''
Takes in a datetime, outputs prediction of immediate momentum for BTC.

Predictions done based on a typical Stochastica Oscillator signal
    https://www.investopedia.com/terms/s/stochasticoscillator.asp
'''
def forecastMomentum(ticker, date):
    start = date - timedelta(days=16)
    granularity = 86400

    # gather data
    time.sleep(2) # prevent overloading coinbase servers
    price_data_csv = market.historical_data_csv(ticker, start.isoformat(), date.isoformat(), granularity)
    df = pandas.read_csv(filepath_or_buffer=price_data_csv.name, delimiter=',', header=0)
    df['time'] = pandas.to_datetime(df.time, unit='s')  # gotta convert those dates to a usable format
    data_frame = pandas.DataFrame(df).set_index('time').sort_values(by='time', ascending=True)

    # Stochastic Oscillator Analysis
    SMA_Period = 3  # typical SMA period for S.O.
    data_frame['Stoch_D'] = momentum.stoch_signal(high=data_frame['high'], low=data_frame['low'],
                                                  close=data_frame['close'], n=14, d_n=SMA_Period, fillna=False)
    data_frame['Stoch_K'] = momentum.stoch(high=data_frame['high'], low=data_frame['low'], close=data_frame['close'],
                                           n=14, d_n=SMA_Period, fillna=False)

    # predict based on signal
    signal = data_frame['Stoch_D'].array[-1] + data_frame['Stoch_K'].array[-1]
    if signal > 160:  # overbought assets
        return 2
    elif signal < 40:  # oversold asset
        return 0
    else:  # not overbought/sold, should hold the asset
        return 1;

    os.remove(price_data_csv.name)
