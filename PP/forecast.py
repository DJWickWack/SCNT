import CB.market as market
from datetime import datetime, timedelta
import pandas
import os
from ta import momentum
import time

'''
Takes in a csv, outputs prediction of immediate momentum for BTC.
Signals indicate some sort of reversal.

Predictions done based on a typical Stochastica Oscillator signal
    https://www.investopedia.com/terms/s/stochasticoscillator.asp
'''
def forecastMomentum(price_data_csv):
    df = pandas.read_csv(filepath_or_buffer=price_data_csv.name, delimiter=',', header=0)
    df['time'] = pandas.to_datetime(df.time, unit='s')  # gotta convert those dates to a usable format
    data_frame = pandas.DataFrame(df).set_index('time').sort_values(by='time', ascending=True)

    # Fast Stochastic Oscillator Check
    SMA_Period = 3  # typical SMA period for S.O.
    data_frame['Stoch_D'] = momentum.stoch_signal(high=data_frame['high'], low=data_frame['low'],
                                                  close=data_frame['close'], n=15, d_n=SMA_Period, fillna=False)
    data_frame['Stoch_K'] = momentum.stoch(high=data_frame['high'], low=data_frame['low'], close=data_frame['close'],
                                           n=15, d_n=SMA_Period, fillna=False)

    data_frame['RSI'] = momentum.rsi(close=data_frame['close'], n=15)

    # predict based on signal
    signal = data_frame['Stoch_D'].array[-1] + data_frame['Stoch_K'].array[-1]
    RSI = data_frame['RSI'].array[-1]
    if signal > 160 and RSI > 70:  # overbought assets
        print(f"\nSO signal: {signal}\nRSI: {RSI}\nCLOSE: {data_frame['close'].array[-1]}")
        return 2
    elif signal < 40 and RSI < 30:  # oversold asset
        print(f"\nSO signal: {signal}\nRSI: {RSI}\nCLOSE: {data_frame['close'].array[-1]}")
        return 0
    else:  # not overbought/sold, should hold the asset
        print(f"\nSO signal: {signal}\nRSI: {RSI}\nCLOSE: {data_frame['close'].array[-1]}")
        return 1