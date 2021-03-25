import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dataClient.production import productionVisualization as pVis

production_layout = html.Div([
    html.H2(children='Production'),
    html.H3(children='Productivity'),
    dcc.Graph(
        id='productivity',
        figure=pVis.getProductivityFigure()
    ),
    html.H3(children='Production Yield'),
    dcc.Graph(
        id='production-yield',
        figure=pVis.getProductionFigure()
    ),
    html.H3(children='Production Orders'),
    html.H4(children='Target Quantity'),
    dcc.Graph(
        id='production-orders-target-quantity',
        figure=pVis.getTargetQuantityFigure()
    ),
    html.H4(children='Confirmed Quantity'),
    dcc.Graph(
        id='production-orders-confirmed-quantity',
        figure=pVis.getConfirmedQuantityFigure()
    ),
    html.H3(children='Purchase Order'),
    dcc.Graph(
        id='purchase-order.figure',
        figure=pVis.getPurchaseOrderFigure()
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='production-content')
])