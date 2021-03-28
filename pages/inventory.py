import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dataClient.inventory import inventoryVisualization as invVis

inventory_layout = html.Div([
    html.H2(children="Inventory"),
    
    html.H3(children="500 g Muesli"),
    html.H4(children="Inventory of 500g Muesli"),
    # Inventory 500 g
    dcc.Graph(
        id="inventory-500",
        figure=invVis.getFigure("500", "Finished Product")
    ),
    html.H3(children="1kg Muesli"),
    html.H4(children="Inventory of 1kg Muesli"),
    # 1 kg Inventory
    dcc.Graph(
        id="inventory-1",
        figure=invVis.getFigure("1", "Finished Product")
    ),
    # Raw materials
    dcc.Graph(
        id="raw-materials",
        figure=invVis.getFigure("", "Raw materials")
    ),
    dcc.Interval(
        id="interval-component",
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id="inventory-content")
])