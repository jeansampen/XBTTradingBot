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

index = 17
line_offest = 1
x0 = df.loc[index - line_offest, 'timestamp']
x1 = df.loc[index + line_offest, 'timestamp']
y = df.loc[index, 'open']

print('x0 = ', x0)
print('x1 = ', x1)
print('y = ', y)


fig.update_layout(
    title='The Great Recession',
    yaxis_title='AAPL Stock',
    shapes=[
        dict(type="line",
            x0=x0,
            y0=y,
            x1=x1,
            y1=y,
            line=dict(
                color="Black",
                width=4,
                dash="dashdot",
            ))],
)

fig.show()
