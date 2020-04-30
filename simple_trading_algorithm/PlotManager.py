import datetime

import plotly.graph_objects as go

from Enum.PriceType import PriceType
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

    fig.update_layout(showlegend=False, xaxis_rangeslider_visible=False)

    return fig


class PlotManager:
    SUPPORT_MARKER_SIZE = 10
    MAIN_MARKER_SIZE = 20
    PRICE_OFFSET = 10
    TIME_OFFSET = datetime.timedelta(minutes=5)
    LINE_WIDTH = 2


    def __init__(self, data_manager):
        self.data_manager: DataManager = data_manager
        self.fig = get_figure(self.data_manager)

    def move_marker(self, x, y, marker_id):
        self.remove_marker_by_id(marker_id)
        self.fig.add_trace(go.Scatter(x=[x],
                                      y=[y],
                                      mode="markers",
                                      ids=[marker_id],
                                      marker=dict(color="blue", size=3)))

    def add_sell_triangle_for_index(self, index):
        [timestamp, price] = self.data_manager.get_data_for_index_and_price_type(index, PriceType.LOW)
        self.add_sell_triangle(timestamp, price)

    def add_buy_triangle_for_index(self, index):
        [timestamp, price] = self.data_manager.get_data_for_index_and_price_type(index, PriceType.LOW)
        self.add_buy_triangle(timestamp, price)

    def add_starting_point_triangle(self):
        [starting_timestamp, starting_price] = self.data_manager.get_starting_point_for_price_type(PriceType.LOW)
        self.add_marker(position_x=starting_timestamp - PlotManager.TIME_OFFSET,
                        position_y=starting_price,
                        color='Blue',
                        direction='triangle-right',
                        text=starting_price,
                        text_position='top center')

    def add_sell_triangle(self, timestamp, price):
        self.add_marker(position_x=timestamp,
                        position_y=price + PlotManager.PRICE_OFFSET,
                        color='Red',
                        direction='triangle-down',
                        text='Sell at ' + str(price),
                        text_position='top center',
                        size=PlotManager.MAIN_MARKER_SIZE)

    def add_buy_triangle(self, timestamp, price):
        self.add_marker(position_x=timestamp,
                        position_y=price - PlotManager.PRICE_OFFSET,
                        color='Green',
                        direction='triangle-up',
                        text='Buy at ' + str(price),
                        text_position='bottom center',
                        size=PlotManager.MAIN_MARKER_SIZE)

    def add_marker(self, position_x, position_y, color, direction, text, text_position, size=SUPPORT_MARKER_SIZE, marker_id='dummy_id'):
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
                    size=size
                ),
                showlegend=False,
                ids=[marker_id]
            )
        )

    def add_buy_line(self, price_level, line_id):
        self.add_horizontal_line(height=price_level, color='Green', line_id=line_id)

    def add_sell_line(self, price_level, line_id):
        self.add_horizontal_line(height=price_level, color='Red', line_id=line_id)

    def add_horizontal_line(self, height, color, line_id='dummy_id'):
        self.fig.add_shape(
            dict(
                type="line",
                x0=self.data_manager.start_index,
                y0=height,
                x1=self.data_manager.end_index,
                y1=height,
                line=dict(
                    color=color,
                    width=PlotManager.LINE_WIDTH,
                    dash='dashdot'
                ),
                templateitemname=line_id,
                visible=True
            ))

        starting_timestamp = self.data_manager.get_starting_point_for_price_type(PriceType.LOW)[0]
        self.add_marker(position_x=starting_timestamp - PlotManager.TIME_OFFSET,
                        position_y=height,
                        color=color,
                        direction='triangle-right',
                        text=height,
                        text_position='middle left', )


    def remove_line_by_id(self, line_id):
        self.fig.layout.shapes = [l for l in self.fig.layout.shapes if not (l.templateitemname == line_id)]

    def remove_marker_by_id(self, marker_id):
        self.fig.data = [m for m in self.fig.data if not (isinstance(m, go.Scatter) and m.ids[0] == marker_id)]
