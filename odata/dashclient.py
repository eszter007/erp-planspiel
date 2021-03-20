# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import service

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Amount": service.inventory.fetch()[2],
    "Date":service.inventory.fetch()[3],
    "Material":service.inventory.fetch()[0]
})

fig = px.bar(df, x="Date", y="Amount", color="Material")

app.layout = html.Div(children=[
    html.H1(children='ERP Planspiel'),

    html.Div(children='''
        A dashboard for monitoring the data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)