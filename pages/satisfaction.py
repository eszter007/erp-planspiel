import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import satisfaction

satisfaction_layout = html.Div([
    html.H2(children='Satisfaction'),
    dcc.Graph(
        id='satisfaction-time',
        figure=satisfaction.satisfactionVisualization.getFigure()
    ), 
    html.Div(id='satisfaction-content')
])