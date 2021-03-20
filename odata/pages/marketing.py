import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import marketing

marketing_layout = html.Div([
    html.H2(children='Marketing'),
    dcc.Graph(
        id='marketing-area',
        figure=marketing.marketingVisualization.getFigureByArea()
    ),
    
    dcc.Graph(
        id='marketing-area',
        figure=marketing.marketingVisualization.getFigureByTime("")
    ),
    
    html.Div(id='marketing-content')
])