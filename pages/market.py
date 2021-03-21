import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import market

market_layout = html.Div([
    html.H2(children='Market'),
    dcc.Graph(
        id='market-per-area-and-material',
        figure=market.marketVisualization.getQuantityPerAreaAndMaterial()
    ),
    dcc.Graph(
        id='market-price-quantitiy',
        figure=market.marketVisualization.getPriceAndAmount()
    ),
    html.Div(id='market-content')
])