import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pages import index, inventory, marketing, company, market, suppliers, satisfaction, sales, production

print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash( __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.config.suppress_callback_exceptions = True

def serve_layout():
    app_layout = html.Div(className='page-container', children=[
        html.H1('ERP Planspiel'),
        html.Div(children='''
            A dashboard for monitoring the data.
        '''),
        html.Div(
                    className='navigation',
                    children=[
                        dbc.Nav([
                            dbc.NavItem(dbc.NavLink("Company KPIs", href="/company")),
                            dbc.NavItem(dbc.NavLink("Sales", href="/sales")),
                            dbc.NavItem(dbc.NavLink("Market", href="/market")),
                            dbc.NavItem(dbc.NavLink("Marketing", href="/marketing")),
                            dbc.NavItem(dbc.NavLink("Inventory", href="/inventory")),
                            dbc.NavItem(dbc.NavLink("Production", href="/production")),
                            dbc.NavItem(dbc.NavLink("Suppliers", href="/suppliers")),
                            dbc.NavItem(dbc.NavLink("Satisfaction", href="/satisfaction"))
                        ],
                            pills=True,
                        )
                    ]
        ),
        html.Div(id='page-content'),
        dcc.Location(id='url', refresh=False),
        html.Div(className='Reminder', children=[
            html.P("Reminder:"),
            html.P("Nut - F01: 500g // F11: 1kg // R01 Nuts"),
            html.P("Blueberry - F02: 500g // F12: 1kg // R02 Blueberries"),
            html.P("Strawberry - F03: 500g // F13: 1kg // R03 Strawberries"),
            html.P("Raisin - F04: 500g // F14: 1kg // R04: Raisins"),
            html.P("Original -  F05: 500g // F15: 1kg // R05: Wheat"),
            html.P("Mixed Fruit - F06: 500g // F16: 1kg // R06: Oats"),
            html.P("P01: Large Box, P02: Large Bag (1kg)"),
            html.P("P03: Small Box, P02: Small Bag (500g)")
        ])
    ])
    
    return app_layout

# Page 1 callback
@app.callback(dash.dependencies.Output('inventory-content', 'children'),
              [dash.dependencies.Input('inventory-content', 'value')])

# Page 2
@app.callback(dash.dependencies.Output('marketing-content', 'children'),
              [dash.dependencies.Input('marketing-content', 'value')])

# Page Company callback
@app.callback(dash.dependencies.Output('company-content', 'children'),
              [dash.dependencies.Input('company-content', 'value')])

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

# Page production callback
@app.callback(dash.dependencies.Output('production-content', 'children'),
              [dash.dependencies.Input('production-content', 'value')])

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
    elif pathname == '/market':
        return market.market_layout
    elif pathname == '/suppliers':
        return suppliers.suppliers_layout
    elif pathname == '/satisfaction':
        return satisfaction.satisfaction_layout
    elif pathname == '/sales':
        return sales.sales_layout
    elif pathname == '/production':
        return production.production_layout
    else:
        return '404'

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)