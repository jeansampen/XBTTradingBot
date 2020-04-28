import datetime

import plotly.graph_objects as go

from simple_trading_algorithm.DataManager import DataManager


def get_figure(data):
    fig = go.Figure(data=[go.Candlestick(x=data['timestamp'],
                                         open=data['open'],
                                         high=data['high'],
                                         low=data['low'],
                                         close=data['close'])])

    fig.update_layout(
        title='XBT Price in the last 1000 minutes',
        yaxis_title='XBT Price (USD)',
        xaxis_title='Time (minutes)'
    )

    return fig


class PlotManager:
    def __init__(self, data_manager):
        self.data_manager: DataManager = data_manager
        self.marker_size = 10
        self.price_offset = 10
        self.time_offset = datetime.timedelta(minutes=5)
        self.line_width = 2
        self.fig = get_figure(self.data_manager.data)

    def add_sell_triangle_to_figure_for_index(self, index):
        [timestamp, price] = self.data_manager.get_data_for_index(index)
        self.add_sell_triangle_to_figure(timestamp, price)

    def add_buy_triangle_to_figure_for_index(self, index):
        [timestamp, price] = self.data_manager.get_data_for_index(index)
        self.add_buy_triangle_to_figure(timestamp, price)

    def add_starting_point_triangle_to_figure(self):
        [starting_timestamp, starting_price] = self.data_manager.get_starting_point()
        self.add_triangle_to_figure(position_x=starting_timestamp - self.time_offset,
                                    position_y=starting_price,
                                    color='Blue',
                                    direction='triangle-right',
                                    text=starting_price,
                                    text_position='top center')

    def add_sell_triangle_to_figure(self, timestamp, price):
        self.add_triangle_to_figure(position_x=timestamp,
                                    position_y=price + self.price_offset,
                                    color='Red',
                                    direction='triangle-down',
                                    text='Sell at ' + str(price),
                                    text_position='top center')

    def add_buy_triangle_to_figure(self, timestamp, price):
        self.add_triangle_to_figure(position_x=timestamp,
                                    position_y=price - self.price_offset,
                                    color='Green',
                                    direction='triangle-up',
                                    text='Buy at ' + str(price),
                                    text_position='bottom center')

    def add_triangle_to_figure(self, position_x, position_y, color, direction, text, text_position):
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

    def add_buy_line_to_figure(self, height):
        self.add_horizontal_line_to_figure(height, color='Red')

    def add_sell_line_to_figure(self, height):
        self.add_horizontal_line_to_figure(height, color='Green')

    def add_horizontal_line_to_figure(self, price_level, color):
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
        self.add_triangle_to_figure(position_x=startin_timestamp - self.time_offset,
                                    position_y=price_level,
                                    color=color,
                                    direction='triangle-right',
                                    text=price_level,
                                    text_position='middle left')

    def add_order_levels_to_figure(self, delta, num_of_layers):
        starting_price = self.data_manager.get_starting_point()[1]
        for i in range(1, num_of_layers + 1):
            # add_buy_line_to_figure(fig=fig, height=starting_price + i * delta)
            self.add_sell_line_to_figure(height=starting_price - i * delta)
