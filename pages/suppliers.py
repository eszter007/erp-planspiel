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
    html.Div(id='suppliers-content')
])