import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dataClient.marketing import marketingVisualization as markVis

marketing_layout = html.Div([
    html.H2(children='Marketing'),
    dcc.Graph(
        id='marketing-area',
        figure=markVis.getFigureByArea()
    ),
    
    dcc.Graph(
        id='marketing-area',
        figure=markVis.getFigureByTime("")
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='marketing-content')
])