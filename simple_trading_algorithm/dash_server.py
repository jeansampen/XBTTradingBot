# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from simple_trading_algorithm.simple_algorithm import *
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

optimiser = Optimiser()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Interval(
        id='simulation-step-interval',
        disabled=True,
        interval=500,
        max_intervals=1000
    ),

    html.Button(children='Start Simulation', id='start-simulation-button'),
    html.Div(id='my-div'),
    dcc.Graph(
        id='candlestick-graph',
        figure=optimiser.figure,
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
def simulation_step(n_intervals):
    print('Iteration #{}'.format(n_intervals))
    optimiser.run_algorithm_step(n_intervals)

    return optimiser.figure


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