import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import index, inventory, marketing, company, material, market, suppliers, satisfaction

print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash( __name__)
server = app.server

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    html.H1('ERP Planspiel'),

    html.Div(children='''
        A dashboard for monitoring the data.
    '''),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Link('Company KPIs   ', href='/company'),
    dcc.Link('Market   ', href='/market'),
    dcc.Link('Marketing   ', href='/marketing'),
    dcc.Link('Inventory   ', href='/inventory'),
    dcc.Link('Material   ', href='/material'),
    dcc.Link('Suppliers   ', href='/suppliers'),
    dcc.Link('Satisfaction   ', href='/satisfaction')
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
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)