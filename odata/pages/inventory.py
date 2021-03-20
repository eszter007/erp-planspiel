import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import inventory

inventory_layout = html.Div([
    html.H2(children='Inventory'),
    # Inventory 500 g
    dcc.Graph(
        id='inventory-500',
        figure=inventory.inventoryVisualization.getFigure("500")
    ),
    
    dcc.Graph(
        id='inventory-1',
        figure=inventory.inventoryVisualization.getFigure("1")
    ),
    
    html.Div(id='inventory-content'),
    html.Br(),
    dcc.Link('Marketing', href='/marketing'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),

])