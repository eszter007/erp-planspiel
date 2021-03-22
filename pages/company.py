import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dataClient.company import companyVisualization as vis

company_layout = html.Div([
    html.H2(children='Company'),
    html.H3(children='Company Valuation'),
    dcc.Graph(
        id='company-valuation',
        figure=vis.getCompanyValuationFigure()
    ),
    html.H3(children='Debt Loading & Profits'),
    dcc.Graph(
        id='company-debt-loading-profits',
        figure=vis.getDebtLoadingProfitsFigure()
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id='company-content')
])