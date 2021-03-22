import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dataClient.sales import salesVisualization as salesVis

sales_layout = html.Div([
    html.H2(children='Sales'),
    html.H3(children='Amount of Products Sold'),
    dcc.Graph(
        id='sales-sold-time',
        figure=salesVis.getAmountSoldFigure()
    ),
    html.H3(children='Margin per Product'),
    dcc.Graph(
        id='sales-margin',
        figure=salesVis.getMarginFigure()
    ),
    html.H3(children='Total Sales per Area'),
    dcc.Graph(
        id='sales-per-area',
        figure=salesVis.getSalePerAreaFigure()
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='sales-content')
])