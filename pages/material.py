import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app.material import materialVisualization as matVis

material_layout = html.Div([
    html.H2(children='Material'),
    html.H3(children="Raw materials"),
    dcc.Graph(
        id='material-raw-ingredients',
        figure=matVis.getFigure("Raw materials", "KG", "")
    ),
    dcc.Graph(
        id='material-raw-packaging',
        figure=matVis.getFigure("Raw materials", "ST", "")
    ),
    html.H3(children="Finished Products"),
    dcc.Graph(
        id='material-quantity-500',
        figure=matVis.getFigure("Finished Product", "", "500")
    ),
    dcc.Graph(
        id='material-quantity-1',
        figure=matVis.getFigure("Finished Product", "", "1kg")
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='material-content')
])