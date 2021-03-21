import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import inventory
import marketing

inventory_layout = html.Div([
    html.H2(children='Inventory'),
    
    html.H3(children='500 g Muesli'),
    # Inventory 500 g
    dcc.Graph(
        id='inventory-500',
        figure=inventory.inventoryVisualization.getFigure("500")
    ),
    
    # Marketing 500 g
    dcc.Graph(
        id='marketing-500',
        figure=marketing.marketingVisualization.getFigureByTime("500")
    ),
    
    html.H3(children='1kg Muesli'),
    # 1 kg Inventory
    dcc.Graph(
        id='inventory-1',
        figure=inventory.inventoryVisualization.getFigure("1")
    ),
    
    # Marketing 1kg
    dcc.Graph(
        id='marketing-1',
        figure=marketing.marketingVisualization.getFigureByTime("1")
    ),
    html.Div(id='inventory-content')
])