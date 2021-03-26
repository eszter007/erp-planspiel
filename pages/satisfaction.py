import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dataClient.satisfaction import satisfactionVisualization as sVis

satisfaction_layout = html.Div([
    html.H2(children="Satisfaction"),
    html.H3(children="Average Customer Satisfaction per Product over Time"),
    dcc.Graph(
        id="satisfaction-time",
        figure=sVis.getFigure()
    ),
    html.H3(children="Average Customer Satisfaction per Area"),
    dcc.Graph(
        id="satisfaction-product-area",
        figure=sVis.getSatisfactionPerAreaFigure()
    ),
    html.H3(children="Average Customer Satisfaction per Product"),
    dcc.Graph(
        id="satisfaction-product",
        figure=sVis.getSatisfactionPerProduct()
    ),
    dcc.Interval(
        id="interval-component",
        interval=1*10000, # in milliseconds
        n_intervals=0
    ), 
    html.Div(id="satisfaction-content")
])