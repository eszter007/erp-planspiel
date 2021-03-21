import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import company

company_layout = html.Div([
    html.H2(children='Company'),
    dcc.Graph(
        id='company-valuation',
        figure=company.companyVisualization.getFigure()
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='company-content')
])