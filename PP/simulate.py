import PP.forecast as forecast
from datetime import datetime, timedelta
import CB.market
import News.search as news
import SentAnalysis

'''
Lets do several forecasts to see what results we get.
Just a basic simulation to see how accurate simple momentum indication is.
'''

# Get list of timestamps for daily candles
base = datetime(year=2020, month=7, day=25, hour=20)
first_day_of_2020 = datetime(year=2020, month=1, day=1, hour=20)
numdays = (base - first_day_of_2020).days +1
date_list = [base - timedelta(days=x) for x in range(numdays)]
date_list.reverse()

granularity = 86400  # Daily candles

current_Holdings_USD = 10000.0
current_Holdings_BTC = 1.0
curr_price_BTC = None

current_Holdings_BTC_sentiment = 1.0
current_Holdings_USD_sentiment = 10000.0

analyzer = SentAnalysis.SentAnalysis()

prev_signal = None
for day in date_list:
    daily_data = forecast.ta_only_forecastMomentum(CB.market.get_forecastable_data('BTC-USD', day, granularity))
    curr_signal = daily_data['signal']
    curr_price_BTC = daily_data['PRICE']
    current_holdings_net = current_Holdings_USD+(current_Holdings_BTC*curr_price_BTC)
    current_holdings_net_sentiment = current_Holdings_USD_sentiment+(current_Holdings_BTC_sentiment*curr_price_BTC)

    if prev_signal is None:
        prev_signal = curr_signal
        continue
    if prev_signal == 2:
        if curr_signal == 1:
            prev_signal = curr_signal

            print(f"ACTION: SELL {(current_Holdings_BTC*0.25)*daily_data['PRICE']} in USD")
            current_Holdings_BTC *= 0.75
            current_Holdings_USD += daily_data['PRICE']*0.25
            print(f"Curr_Holdings: {current_holdings_net}")

            # check sentiment decision
            articles = news.NewsDaySearch('bitcoin', day, timedelta(days=1))
            sentiments = analyzer.newsAnalysis(articles)
            average = 0
            for sent in sentiments:
                if sent != 0.0:
                    average += sent
            average = average/len(sentiments)
            if average < 0.08:
                print(f"ACTION: SELL(sent: {average}) {(current_Holdings_BTC_sentiment * 0.25) * daily_data['PRICE']} in USD")
                current_Holdings_BTC_sentiment *= 0.75
                current_Holdings_USD_sentiment += daily_data['PRICE'] * 0.25
                print(f"Curr_Holdings: {current_holdings_net_sentiment}")
            else:
                print(f"ACTION: wait(sent: {average})")
                print(f"Curr_Holdings(sent): {current_holdings_net_sentiment}")

            print(f'DATE: {day.date()}')
            continue
        elif curr_signal == 0 or curr_signal == 2:
            prev_signal = curr_signal
            print("wait")
            print(f'DATE: {day.date()}')
            continue
        else:
            raise Exception('No Signal Or Invalid Signal Found')
    if prev_signal == 1:
        prev_signal = curr_signal
        print('ACTION: wait')
        print(f'DATE: {day.date()}')
        continue
    if prev_signal == 0:
        if curr_signal == 1:
            prev_signal = curr_signal

            print(f'ACTION: BUY {current_Holdings_USD*0.25} in BTC')
            current_Holdings_BTC += daily_data['PRICE']/(current_Holdings_USD*0.25)
            current_Holdings_USD *= 0.75
            print(f"Curr_Holdings: {current_holdings_net}")

            # check sentiment decision
            articles = news.NewsDaySearch('bitcoin', day, timedelta(days=1))
            sentiments = analyzer.newsAnalysis(articles)
            average = 0
            for sent in sentiments:
                if sent != 0.0:
                    average += sent
            average = average / len(sentiments)
            if average > 0:
                print(f'ACTION: BUY(sent): {average}) {current_Holdings_USD_sentiment * 0.25} in BTC')
                current_Holdings_BTC_sentiment += daily_data['PRICE'] / (current_Holdings_USD_sentiment * 0.25)
                current_Holdings_USD_sentiment *= 0.75
                print(f"Curr_Holdings(sent): {current_holdings_net_sentiment}")
            else:
                print(f"ACTION: wait(sent: {average})")
                print(f"Curr_Holdings(sent): {current_holdings_net_sentiment}")

            print(f'DATE: {day.date()}')
            continue
        elif curr_signal == 2 or curr_signal == 0:
            prev_signal = curr_signal
            print('ACTION: wait')
            print(f'DATE: {day.date()}')
            continue
    raise Exception('Should not have gotten here')

print(f'Result of only TA: {current_Holdings_USD + (current_Holdings_BTC*curr_price_BTC)} total assets in USD')
print(f'Result TA with Sentiment: {current_Holdings_USD_sentiment + (current_Holdings_BTC_sentiment*curr_price_BTC)} total assets in USD')
