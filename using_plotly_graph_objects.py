import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

print('Loading data from CSV')
df = pd.read_csv('data/bitstamp.csv')[-10000:]





print("Creating Figure")
fig = go.Figure(data=[go.Candlestick(x=df['Timestamp'].map(datetime.fromtimestamp),
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

print('Showing....')
fig.show()