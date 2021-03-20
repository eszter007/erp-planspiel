import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import marketing

marketing_layout = html.Div([
    html.H2(children='Marketing'),
    # Marketing 500 g
    dcc.Graph(
        id='marketing-500',
        figure=marketing.marketingVisualization.getFigure("500")
    ),
    
    dcc.Graph(
        id='marketing-1',
        figure=marketing.marketingVisualization.getFigure("1")
    ),
    
    html.Div(id='marketing-content'),
    html.Br(),
    dcc.Link('Inventory', href='/inventory'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),

])