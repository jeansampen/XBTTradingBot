# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from simple_trading_algorithm.simple_algorithm import *
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

optimiser = Optimiser()
current_price = 0
current_time = 0
current_balance = 0

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Interval(
        id='simulation-step-interval',
        disabled=True,
        interval=100,
        max_intervals=1000
    ),

    html.Button(children='Start Simulation', id='start-simulation-button'),
    html.Div(style={
        'fontSize': 20,
        'fontWeight': 'bold',
        'textAlign': 'center'
    }, children=[
        html.Div(id='time-div', children='Time = '),
        html.Div(id='price-div', children='Price = '),
        html.Div(id='balance-div', children='Balance = ')
    ]),
    dcc.Graph(
        id='candlestick-graph',
        figure=optimiser.figure,
        style={
            'height': 1500
        }
    )
])


@app.callback(
    [
        Output(component_id='candlestick-graph', component_property='figure'),
        Output(component_id='time-div', component_property='children'),
        Output(component_id='price-div', component_property='children'),
        Output(component_id='balance-div', component_property='children')
    ],
    [
        Input('simulation-step-interval', 'n_intervals')
    ]
)
def simulation_step(n_intervals):
    global current_balance, current_price, current_time
    if n_intervals is not None and 0 < n_intervals < optimiser.data_manager.MAX_INDEX:
        print('Iteration #{}'.format(n_intervals))
        [current_time, current_price, current_balance] = optimiser.run_algorithm_step(n_intervals)

    return [optimiser.figure, 'Time = ' + str(current_time), 'Close Price = ' + str(current_price), 'Balance = ' + str(current_balance)]


@app.callback(
    [
        Output(component_id='simulation-step-interval', component_property='disabled'),
        Output(component_id='start-simulation-button', component_property='children')
    ],
    [
        Input('start-simulation-button', 'n_clicks'),
    ]
)
def on_start_simulation_click(n_clicks):
    print('Start simulation callback invoked')
    if n_clicks is not None and n_clicks == 1:
        print('Starting the simulation')
        return [False, 'Restart Simulation']
    elif n_clicks is None:
        print('Page just loaded for the first time. Waiting for first button click')
        return [True, 'Start Simulation']
    else:
        print('Simulation was already executed. Not running a new simulation')
        return [True, 'Start Simulation']


if __name__ == '__main__':
    app.run_server(debug=True)