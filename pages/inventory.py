import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app.inventory import inventoryVisualization as invVis
from app.marketing import marketingVisualization as markVis

inventory_layout = html.Div([
    html.H2(children='Inventory'),
    
    html.H3(children='500 g Muesli'),
    # Inventory 500 g
    dcc.Graph(
        id='inventory-500',
        figure=invVis.getFigure("500")
    ),
    
    # Marketing 500 g
    dcc.Graph(
        id='marketing-500',
        figure=markVis.getFigureByTime("500")
    ),
    
    html.H3(children='1kg Muesli'),
    # 1 kg Inventory
    dcc.Graph(
        id='inventory-1',
        figure=invVis.getFigure("1")
    ),
    
    # Marketing 1kg
    dcc.Graph(
        id='marketing-1',
        figure=markVis.getFigureByTime("1")
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='inventory-content')
])