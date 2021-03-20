import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import inventory

overview_layout = html.Div([
    html.H1('ERP'),
    html.H1(children='ERP Planspiel'),

    html.Div(children='''
        A dashboard for monitoring the data.
    '''),
    
    html.Div(id='inventory-content'),
    html.Br(),
    dcc.Link('Marketing', href='/marketing'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),

])