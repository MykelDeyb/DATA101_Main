from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

# Initializing your Dash application
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create layout for each page
page1_layout = html.Div([
    html.H1('CMCI HUB'),
    html.P('Explore CMCI Data with Ease')
])

page2_layout = html.Div([
    html.H1('VISUALIZATION DASHBOARD'),
    html.P('This is page 2.')
])

page3_layout = html.Div([
    html.H1('INTERACTIVE MAP'),
    html.P('This is page 3.')
])

# Define navigation bar
navbar = dbc.NavbarSimple(
    children=[
        html.Div(
            [
                dbc.Button("CMCI HUB", href="/page-1", color="primary", className="mr-1"),
                dbc.Button("VISUALIZATION DASHBOARD", href="/page-2", color="primary", className="mr-1"),
                dbc.Button("INTERACTIVE MAP", href="/page-3", color="primary")
            ],
            className="d-flex justify-content-center"  # Center the buttons horizontally
        )
    ],
    color="dark",  # Set navigation bar color to dark
    dark=True,  # Use dark theme for navigation bar
    style={"font-family": "Arial, sans-serif", "font-weight": "bold", "color": "black"}  # Apply font style
)

# Define callback to update page content based on URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/page-1':  # Check if the pathname is empty or '/page-1'
        return page1_layout
    elif pathname == '/page-2':
        return page2_layout
    elif pathname == '/page-3':
        return page3_layout
    else:
        return '404 - Page not found'

# Layout of the entire app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

if __name__ == '__main__':
    app.run_server(debug=True)
