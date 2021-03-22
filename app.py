import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import index, inventory, marketing, company, material, market, suppliers, satisfaction, sales

print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash( __name__)
server = app.server

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    html.H1('ERP Planspiel'),

    html.Div(children='''
        A dashboard for monitoring the data.
    '''),
    html.Div(id='page-content'),
    dcc.Link('Company KPIs   ', href='/company'),
    dcc.Link('Market   ', href='/market'),
    dcc.Link('Marketing   ', href='/marketing'),
    dcc.Link('Inventory   ', href='/inventory'),
    dcc.Link('Material   ', href='/material'),
    dcc.Link('Suppliers   ', href='/suppliers'),
    dcc.Link('Satisfaction   ', href='/satisfaction'),
    dcc.Link('Sales   ', href='/sales'),
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.P("Reminder:"),
        html.P("Nut - F01: 500g // F11: 1kg // R01 Nuts"),
        html.P("Blueberry - F02: 500g // F12: 1kg // R02 Blueberries"),
        html.P("Strawberry - F03: 500g // F13: 1kg // R03 Strawberries"),
        html.P("Raisin - F04: 500g // F14: 1kg // R04: Raisins"),
        html.P("Original Fruit -  F05: 500g // F15: 1kg // R05: Wheat"),
        html.P("Mixed Fruit - F06: 500g // F16: 1kg // R06: Oats"),
        html.P("P01: Large Box, P02: Large Bag (1kg)"),
        html.P("P03: Small Box, P02: Small Bag (500g)")
    ])
])

# Page 1 callback
@app.callback(dash.dependencies.Output('inventory-content', 'children'),
              [dash.dependencies.Input('inventory-content', 'value')])

# Page 2
@app.callback(dash.dependencies.Output('marketing-content', 'children'),
              [dash.dependencies.Input('marketing-content', 'value')])

# Page Company callback
@app.callback(dash.dependencies.Output('company-content', 'children'),
              [dash.dependencies.Input('company-content', 'value')])

# Page Material callback
@app.callback(dash.dependencies.Output('material-content', 'children'),
              [dash.dependencies.Input('material-content', 'value')])

# Page Market callback
@app.callback(dash.dependencies.Output('market-content', 'children'),
              [dash.dependencies.Input('market-content', 'value')])

# Page suppliers callback
@app.callback(dash.dependencies.Output('suppliers-content', 'children'),
              [dash.dependencies.Input('suppliers-content', 'value')])

# Page satisfaction callback
@app.callback(dash.dependencies.Output('satisfaction-content', 'children'),
              [dash.dependencies.Input('satisfaction-content', 'value')])

# Page sales callback
@app.callback(dash.dependencies.Output('sales-content', 'children'),
              [dash.dependencies.Input('sales-content', 'value')])

# Index Page callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/inventory':
        return inventory.inventory_layout
    elif pathname == '/marketing':
        return marketing.marketing_layout
    elif pathname == '/company':
        return company.company_layout
    elif pathname == '/material':
        return material.material_layout
    elif pathname == '/market':
        return market.market_layout
    elif pathname == '/suppliers':
        return suppliers.suppliers_layout
    elif pathname == '/satisfaction':
        return satisfaction.satisfaction_layout
    elif pathname == '/sales':
        return sales.sales_layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)