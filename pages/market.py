import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app.market import marketVisualization as marketVis

market_layout = html.Div([
    html.H2(children='Market'),
    dcc.Graph(
        id='market-per-area-and-material',
        figure=marketVis.getQuantityPerAreaAndMaterial()
    ),
    dcc.Graph(
        id='market-price-quantitiy',
        figure=marketVis.getPriceAndAmount()
    ),
    dcc.Graph(
        id='market-price-averages',
        figure=marketVis.getAveragePrice()
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='market-content')
])