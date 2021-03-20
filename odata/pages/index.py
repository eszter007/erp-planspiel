import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

index_page = html.Div([
    dcc.Link('Inventory', href='/inventory'),
    html.Br(),
    dcc.Link('Marketing', href='/marketing'),
])