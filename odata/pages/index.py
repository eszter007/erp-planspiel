import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

index_page = html.Div([
    html.Div(id='page-content'),
    html.Br(),
    dcc.Link('Inventory', href='/inventory'),
    html.Br(),
    dcc.Link('Marketing', href='/marketing'),
    html.Br(),
    dcc.Link('Company KPIs', href='/company'),
    html.Br(),
    dcc.Link('Material', href='/material'),
    html.Br(),
    dcc.Link('Market', href='/market')
])