# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# dash
import dash
import dash_core_components as dcc
import dash_html_components as html

#classes
import service
import inventory

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(children=[
    html.H1(children='ERP Planspiel'),

    html.Div(children='''
        A dashboard for monitoring the data.
    '''),
    
    html.H2(children='Inventory'),
    # Inventory 500 g
    dcc.Graph(
        id='inventory-500',
        figure=inventory.inventoryVisualization.getFigure("500")
    ),
    
    dcc.Graph(
        id='inventory-1',
        figure=inventory.inventoryVisualization.getFigure("1")
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)