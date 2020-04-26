# -*- coding: utf-8 -*-
import time

import dash
import dash_core_components as dcc
import dash_html_components as html
from simple_trading_algorithm.plot_figures import get_figure, update_figure

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

figure = get_figure()

update_figure(figure)


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=figure
    )
])

print('Sleeping...')
time.sleep(3)

if __name__ == '__main__':
    app.run_server(debug=True)