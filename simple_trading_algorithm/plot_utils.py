import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('../bitmex_api_data/trade_bucketed.csv')


def get_data_for_index(index):
    res_x = df.loc[index, 'timestamp']
    res_y = df.loc[index, selected_column]
    return [res_x, res_y]


selected_column = 'low'
marker_size = 30
offset = 10
line_width = 2
start_index = get_data_for_index(0)[0]
end_index = get_data_for_index(999)[0]


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





def add_sell_triangle_to_figure_for_index(fig, index):
    [timestamp, price] = get_data_for_index(index)
    add_sell_triangle_to_figure(fig, timestamp, price)


def add_buy_triangle_to_figure_for_index(fig, index):
    [timestamp, price] = get_data_for_index(index)
    add_buy_triangle_to_figure(fig, timestamp, price)


def add_sell_triangle_to_figure(fig, timestamp, price):
    add_triangle_to_figure(fig=fig,
                           position_x=timestamp,
                           position_y=price + offset,
                           color='Red',
                           direction='triangle-down',
                           size=marker_size,
                           text=price,
                           text_position='top center')


def add_buy_triangle_to_figure(fig, timestamp, price):
    add_triangle_to_figure(fig=fig,
                           position_x=timestamp,
                           position_y=price - offset,
                           color='Green',
                           direction='triangle-up',
                           size=marker_size,
                           text=price,
                           text_position='bottom center')


def add_triangle_to_figure(fig, position_x, position_y, color, direction, size, text, text_position):
    fig.add_trace(
        go.Scatter(
            mode='markers+text',
            x=[position_x],
            y=[position_y],
            text=[text],
            textposition=text_position,
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



def add_buy_line_to_figure(fig, height):
    add_horizontal_line_to_figure(fig, height, color='Red')


def add_sell_line_to_figure(fig, height):
    add_horizontal_line_to_figure(fig, height, color='Green')



def add_horizontal_line_to_figure(fig, height, color):

    fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=start_index,
            y0=height,
            x1=end_index,
            y1=height,
            line=dict(
                color=color,
                width=line_width,
                dash='dashdot'
            )
        ))
