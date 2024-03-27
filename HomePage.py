from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import geopandas as gpd
import pandas as pd
from pathlib import Path

# Initializing your Dash application
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# You can make variables for your components / sections
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
    ],
    brand="PH Educational Institutions",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div(children=[
    navbar, # and add them to the layout
    dbc.Container(children=[
        dbc.Row(children=[
            html.H1("Philippine Educational Institutions"),
            html.P("Education is important and it helps ...."),
            html.P("Second paragraph here.")
        ]),
        dbc.Row(children=[
            html.H2("Which province has more schools?"),
        ]),
        dbc.Row(children=[
           dbc.Col(children=[
               html.P("Choose a column to display"),
               dbc.RadioItems(['amenity', 'operator'], 'amenity', id='map-type', inline=True)
           ], width=6),
           dbc.Col(children=[
               html.P("Choose the value to be displayed on the choropleth:"),
               dcc.Dropdown(['college', 'kindergarten', 'school', 'university'], 'college', id="choropleth-select")
           ], width=6)
        ]),
        dbc.Row(children=[
            dbc.Col(children=[
                dcc.Loading(id="map-loading", children=dcc.Graph(id="map-graph"))
            ], width=6),
            dbc.Col(children=[
                dcc.Loading(id="bar-loading", children=dcc.Graph(id="bar-list"))
            ], width=6)
        ])
    ])
])

if __name__ == '__main__':
    app.run(debug=True)