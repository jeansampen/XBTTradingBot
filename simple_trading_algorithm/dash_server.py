# -*- coding: utf-8 -*-
import time

import dash
import dash_core_components as dcc
import dash_html_components as html
from simple_trading_algorithm.simple_algorithm import *
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

figure = init_figure()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Button('Click Me', id='my-button'),
    html.Div(id='my-div'),
    dcc.Graph(
        id='candlestick-graph',
        figure=figure,
        style={
            'height': 1500
        }
    )
])


@app.callback(
    Output(component_id='candlestick-graph', component_property='figure'),
    [Input('my-button', 'n_clicks')]
)
def on_click(n_clicks):
    if n_clicks is not None and n_clicks > 0:
        add_order_levels_to_figure(fig=figure, delta=25, num_of_layers=5)

    return figure


if __name__ == '__main__':
    app.run_server(debug=True)