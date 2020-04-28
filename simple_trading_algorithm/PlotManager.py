import datetime

import plotly.graph_objects as go

from simple_trading_algorithm.DataManager import DataManager


def get_figure(data_manager):
    static_candlestick_chart = go.Candlestick(x=data_manager.data['timestamp'],
                                              open=data_manager.data['open'],
                                              high=data_manager.data['high'],
                                              low=data_manager.data['low'],
                                              close=data_manager.data['close'])

    static_layout = go.Layout(title='XBT Price in the last 1000 minutes',
                              yaxis_title='XBT Price (USD)',
                              xaxis_title='Time (minutes)')

    fig: go.Figure = go.Figure(data=[static_candlestick_chart],
                               layout=static_layout)

    return fig


class PlotManager:
    def __init__(self, data_manager):
        self.data_manager: DataManager = data_manager
        self.fig = get_figure(self.data_manager)
        self.marker_size = 10
        self.price_offset = 10
        self.time_offset = datetime.timedelta(minutes=5)
        self.line_width = 2

    def move_marker(self, x, y):
        self.fig.data = [
            self.fig.data[0]
        ]
        self.fig.add_trace(go.Scatter(x=[x],
                                      y=[y],
                                      mode="markers",
                                      marker=dict(color="blue", size=20)))

    def add_sell_triangle_for_index(self, index):
        [timestamp, price] = self.data_manager.get_data_for_index(index)
        self.add_sell_triangle(timestamp, price)

    def add_buy_triangle_for_index(self, index):
        [timestamp, price] = self.data_manager.get_data_for_index(index)
        self.add_buy_triangle(timestamp, price)

    def add_starting_point_triangle(self):
        [starting_timestamp, starting_price] = self.data_manager.get_starting_point()
        self.add_triangle(position_x=starting_timestamp - self.time_offset,
                          position_y=starting_price,
                          color='Blue',
                          direction='triangle-right',
                          text=starting_price,
                          text_position='top center')

    def add_sell_triangle(self, timestamp, price):
        self.add_triangle(position_x=timestamp,
                          position_y=price + self.price_offset,
                          color='Red',
                          direction='triangle-down',
                          text='Sell at ' + str(price),
                          text_position='top center')

    def add_buy_triangle(self, timestamp, price):
        self.add_triangle(position_x=timestamp,
                          position_y=price - self.price_offset,
                          color='Green',
                          direction='triangle-up',
                          text='Buy at ' + str(price),
                          text_position='bottom center')

    def add_triangle(self, position_x, position_y, color, direction, text, text_position):
        self.fig.add_trace(
            go.Scatter(
                mode='markers+text',
                x=[position_x],
                y=[position_y],
                text=[text],
                textposition=text_position,
                marker=dict(
                    symbol=direction,
                    color=color,
                    size=self.marker_size
                ),
                showlegend=False
            )
        )

    def add_buy_line(self, height):
        self.add_horizontal_line(height, color='Green')

    def add_sell_line(self, height):
        self.add_horizontal_line(height, color='Red')

    def add_horizontal_line(self, price_level, color):
        self.fig.add_shape(
            # Line Vertical
            dict(
                type="line",
                x0=self.data_manager.start_index,
                y0=price_level,
                x1=self.data_manager.end_index,
                y1=price_level,
                line=dict(
                    color=color,
                    width=self.line_width,
                    dash='dashdot'
                )
            ))

        startin_timestamp = self.data_manager.get_starting_point()[0]
        self.add_triangle(position_x=startin_timestamp - self.time_offset,
                          position_y=price_level,
                          color=color,
                          direction='triangle-right',
                          text=price_level,
                          text_position='middle left')

    def add_order_levels(self, delta, num_of_layers):
        starting_price = self.data_manager.get_starting_point()[1]
        for i in range(1, num_of_layers + 1):
            # add_buy_line(fig=fig, height=starting_price + i * delta)
            self.add_sell_line(height=starting_price - i * delta)
