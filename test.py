import dash
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from openpyxl import load_workbook
from pathlib import Path
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import geopandas as gpd
import numpy as npth
import plotly.graph_objects as go
import numpy as np
import copy
from dash.dependencies import Input, Output, State

popup_modal = dbc.Modal(
    id='popup-modal',
    children=[
        dbc.ModalHeader("Reminder"),
        dbc.ModalBody("Please choose province/LGU in the sidebar on the right."),
        dbc.ModalFooter(
            dbc.Button("OK", id="close-popup-button", className="ml-auto")
        ),
    ],
    is_open=False,
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    popup_modal
])


@app.callback(
    Output("popup-modal", "is_open"),
    [Input("url", "pathname")],
    [State("popup-modal", "is_open")]
)
def toggle_popup(pathname, is_open):
    print("Pathname:", pathname)
    if pathname == "/page-2":
        print("Showing popup modal")
        return True
    return False if is_open else True

@app.callback(
    Output("popup-modal", "is_open"),
    [Input("close-popup-button", "n_clicks")],
    [State("popup-modal", "is_open")]
)
def close_popup(n_clicks, is_open):
    print("Close button clicks:", n_clicks)
    if n_clicks is not None:  # Check if the button has been clicked
        return False  # Close the popup when the button is clicked
    return is_open  # Keep the popup open otherwise


if __name__ == '__main__':
    app.run_server(debug=False)