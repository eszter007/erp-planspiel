import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import suppliers

suppliers_layout = html.Div([
    html.H2(children='Suppliers'),
    dcc.Graph(
        id='suppliersPerTime',
        figure=suppliers.supplierVisualization.getFigure()
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='suppliers-content')
])