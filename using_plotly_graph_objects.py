import plotly.graph_objects as go

import pandas as pd

print('Loading static_test_data from CSV')
df = pd.read_csv('bitmex_api_data/trade_bucketed.csv')


print("Creating Figure")
fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

print('Showing....')

fig.update_layout(
    title='The Great Recession',
    yaxis_title='AAPL Stock',
    shapes = [dict(
        x0='2020-04-26T13:10:00.000Z', x1='2020-04-26T13:11:00.000Z', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2020-04-26T13:10:00.000Z', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase Period Begins')]
)

fig.show()
