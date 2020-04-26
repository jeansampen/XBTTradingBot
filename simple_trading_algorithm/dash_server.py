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

    dcc.Interval(
        id='simulation-step-interval',
        disabled=True,
        interval=1000,
        max_intervals=9
    ),

    html.Button('Start Simulation', id='start-simulation-button'),
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
    [
        Input('simulation-step-interval', 'n_intervals')
    ]
)
def on_start_simulation_click(n_intervals):
    print('Interval callback invoked')
    if n_intervals is not None and 10 > n_intervals > 0:
        print('Running a step {} out of 9 of simulation'.format(n_intervals))
        index = 100 * n_intervals
        add_buy_triangle_to_figure_for_index(figure, index)
    elif n_intervals is None:
        print('This is the initial load. Not executing as we are waiting for a button click')
    else:
        print('We have already gone through 9 steps. No more steps included')

    return figure


@app.callback(
    Output(component_id='simulation-step-interval', component_property='disabled'),
    [
        Input('start-simulation-button', 'n_clicks')
    ]
)
def on_start_simulation_click(n_clicks):
    print('Start simulation callback invoked')
    if n_clicks is not None and n_clicks == 1:
        print('Starting the simulation')
        return False
    elif n_clicks is None:
        print('Page just loaded for the first time. Waiting for first button click')
        return True
    else:
        print('Simulation was already executed. Not running a new simulation')
        return True


if __name__ == '__main__':
    app.run_server(debug=True)