import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dataClient.market import marketVisualization as marketVis

market_layout = html.Div([
    html.H2(children="Market"),
    html.H3(children="Most Popular Products"),
    dcc.Graph(
        id="market-popularity",
        figure=marketVis.getMostPopularProduct()
    ),
    html.H3(children="Popular Products per Area"),
    dcc.Graph(
        id="market-per-area-and-material",
        figure=marketVis.getQuantityPerAreaAndMaterial()
    ),
    html.H3(children="Demand at Prices"),
    dcc.Graph(
        id="market-price-quantitiy",
        figure=marketVis.getPriceAndAmount()
    ),
    html.H3(children="Price Ranges (Entire time)"),
    dcc.Graph(
        id="market-price-averages",
        figure=marketVis.getAveragePrice()
    ),
    html.H3(children="Data per Period"),
    html.H4(children="Price per Period"),
    dcc.Graph(
        id="market-price-time",
        figure=marketVis.getPricesOverTime()
    ),
    html.H4(children="Popularity (Sold Quantity) per Period"),
    dcc.Graph(
        id="market-quantity-period",
        figure=marketVis.getPopularityOverTime()
    ),
    html.H4(children="Purchase Volume of Customers per Period"),
    dcc.Graph(
        id="market-customers-period",
        figure=marketVis.getPurchaseVolumePeriodsFigure()
    ),
    dcc.Interval(
        id="interval-component",
        interval=1*10000, # in milliseconds
        n_intervals=0
    ),
    html.Div(id="market-content")
])