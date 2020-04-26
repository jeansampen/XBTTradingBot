import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('bitmex_api_data/trade_bucketed.csv')

selected_column = 'low'
marker_size = 30
offset = 10


def get_figure():
    print('Loading static_test_data from CSV')

    print("Creating Figure")
    fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                                         open=df['open'],
                                         high=df['high'],
                                         low=df['low'],
                                         close=df['close'])])

    fig.update_layout(
        title='XBT Price in the last 1000 minutes',
        yaxis_title='XBT Price (USD)',
        xaxis_title='Time (minutes)'
    )

    return fig


def get_data_for_index(index):
    res_x = df.loc[index, 'timestamp']
    res_y = df.loc[index, selected_column]
    return [res_x, res_y]


def add_sell_triangle_to_figure_for_index(fig, index):
    [x, y] = get_data_for_index(index)
    add_sell_triangle_to_figure(fig, x, y)


def add_buy_triangle_to_figure_for_index(fig, index):
    [x, y] = get_data_for_index(index)
    add_buy_triangle_to_figure(fig, x, y)


def add_sell_triangle_to_figure(fig, position_x, position_y):
    add_triangle_to_figure(fig, position_x, position_y + offset, color='Red', direction='triangle-down', size=marker_size)


def add_buy_triangle_to_figure(fig, position_x, position_y):
    add_triangle_to_figure(fig, position_x, position_y - offset, color='Green', direction='triangle-up', size=marker_size)


def add_triangle_to_figure(fig, position_x, position_y, color, direction, size):
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=[position_x],
            y=[position_y],
            marker=dict(
                symbol=direction,
                color=color,
                size=size,
                line=dict(
                    color='MediumPurple',
                    width=2
                )
            ),
            showlegend=False
        )
    )

def update_figure(fig):
    index = 17
    line_offest = 1
    x0 = df.loc[index - line_offest, 'timestamp']
    x1 = df.loc[index + line_offest, 'timestamp']
    y = df.loc[index, selected_column]
    fig.add_trace(
        go.Scatter(
            mode='markers',
            x=[x0],
            y=[y],
            marker=dict(
                symbol='triangle-up',
                color='LightSkyBlue',
                size=50,
                line=dict(
                    color='MediumPurple',
                    width=2
                )
            ),
            showlegend=False
        )
    )


index_1 = 17
index_2 = 100

figure = get_figure()
add_buy_triangle_to_figure_for_index(figure, index_1)
add_sell_triangle_to_figure_for_index(figure, index_2)
figure.show()






