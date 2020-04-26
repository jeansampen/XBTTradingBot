# python_candlestick_chart.py
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates

plt.style.use('ggplot')

# Extracting Data for plotting
data = pd.read_csv('static_test_data/data.csv')
ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
ohlc['Date'] = pd.to_datetime(ohlc['Date'])
ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)


bitcoin = pd.read_csv('static_test_data/small_version.csv').loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
bitcoin['Date'] = bitcoin['Date'].map(datetime.fromtimestamp)

# Creating Subplots
fig, ax = plt.subplots()

candlestick_ohlc(ax, bitcoin.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

# Setting labels & titles
ax.set_xlabel('Date')
ax.set_ylabel('Price')
fig.suptitle('Daily Candlestick Chart of NIFTY50')

# Formatting Date
date_format = matplotlib.dates.DateFormatter('%d-%m-%Y %H:%M')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

fig.tight_layout()

plt.show()