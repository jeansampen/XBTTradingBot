from Enum.PriceType import PriceType
from simple_trading_algorithm.DataManager import DataManager
from simple_trading_algorithm.PlotManager import get_figure
import plotly.graph_objects as go


data_manager = DataManager()
figure = get_figure(data_manager)

[x1, y1] = data_manager.get_data_for_index_and_price_type(100, PriceType.LOW)
[x2, y2] = data_manager.get_data_for_index_and_price_type(200, PriceType.LOW)
[x3, y3] = data_manager.get_data_for_index_and_price_type(300, PriceType.LOW)

figure.add_trace(
            go.Scatter(
                mode='markers+text',
                x=[x1],
                y=[y1],
                text=['MARKER_1'],
                textposition='top center',
                marker=dict(
                    symbol='triangle-down',
                    color='Red',
                    size=20
                ),
                showlegend=False,
                ids=['marker1']
            )
        )

figure.add_trace(
            go.Scatter(
                mode='markers+text',
                x=[x2],
                y=[y2],
                text=['MARKER_2'],
                textposition='top center',
                marker=dict(
                    symbol='triangle-down',
                    color='Green',
                    size=20
                ),
                showlegend=False,
                ids=['marker2']
            )
        )


figure.add_trace(
            go.Scatter(
                mode='markers+text',
                x=[x3],
                y=[y3],
                text=['MARKER_3'],
                textposition='top center',
                marker=dict(
                    symbol='triangle-down',
                    color='Blue',
                    size=20
                ),
                showlegend=False,
                ids=['marker3']
            )
        )


marker_id = 'marker3'

figure.data = [m for m in figure.data if not (isinstance(m, go.Scatter) and m.ids[0] == marker_id)]


print('Hello')
figure.show()

