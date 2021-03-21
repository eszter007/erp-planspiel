import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dataClient.satisfaction import satisfactionVisualization as sVis

satisfaction_layout = html.Div([
    html.H2(children='Satisfaction'),
    dcc.Graph(
        id='satisfaction-time',
        figure=sVis.getFigure()
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ), 
    html.Div(id='satisfaction-content')
])