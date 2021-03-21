import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import material

material_layout = html.Div([
    html.H2(children='Material'),
    html.H3(children="Raw materials"),
    dcc.Graph(
        id='material-raw-ingredients',
        figure=material.materialVisualization.getFigure("Raw materials", "KG", "")
    ),
    dcc.Graph(
        id='material-raw-packaging',
        figure=material.materialVisualization.getFigure("Raw materials", "ST", "")
    ),
    html.H3(children="Finished Products"),
    dcc.Graph(
        id='material-quantity-500',
        figure=material.materialVisualization.getFigure("Finished Product", "", "500")
    ),
    dcc.Graph(
        id='material-quantity-1',
        figure=material.materialVisualization.getFigure("Finished Product", "", "1kg")
    ),
    html.Div(id='material-content')
])