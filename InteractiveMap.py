import dash
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from openpyxl import load_workbook
from pathlib import Path

dataset_folder = Path('Datasets/')
workbook_LGU = load_workbook(dataset_folder / 'InteractiveMap_Data/InteractiveMap_Profile.xlsx')

# LGU Profile
lgu_sheet = workbook_LGU['LGU']

lgu = []
category = []
percentage = []
province = []
revenue = []

for row in lgu_sheet.iter_rows(min_row=2, values_only=True):
    lgu.append(row[0])
    category.append(row[1])
    percentage.append(row[2])
    province.append(row[3])
    revenue.append(row[4])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    
    dbc.Row([

    # First column 
    dbc.Col([
        html.Div([
            html.H3('Interactive Map', style={'text-align': 'center', 'margin-bottom': '10px'}),
            # Placeholder for Interactive Map
        ])
    ]),
    # Second column
    dbc.Col([
        html.Div([
            html.H3('LGU Profile', style={'text-align': 'center'}),

            dbc.Row([

            # LGU Dropdown
            html.Label('Select LGU'),
            dcc.Dropdown(
                id='lgu-dropdown',
                options=[{'label': lgu, 'value': lgu} for lgu in lgu],
                value=[]
            ),
            # Pillar Dropdown
            dbc.Row([
                dbc.Col([
                html.Label('Select Pillar'),
                dcc.Dropdown(
                    id='pillar-dropdown',
                    options=[
                            {'label': 'Resiliency', 'value': 'Resiliency'},
                            {'label': 'Government Efficiency', 'value': 'Government Efficiency'},
                            {'label': 'Innovation', 'value': 'Innovation'},
                            {'label': 'Economic Dynamism', 'value': 'Economic Dynamism'},
                            {'label': 'Infrastructure', 'value': 'Infrastructure'},
                            ],
                    value=[]
                ),
                ]),
                dbc.Col([
                html.Label('Pillar Description'),
                ])
            ], style={'margin-left': '20px'}),
            # LGU Profile
            dbc.Row([
                dbc.Col([
                html.Label('Province'),
                ]),
                dbc.Col([
                html.Label('Category'),
                ]),
                dbc.Col([
                html.Label('Revenue'),
                ])
            ], style={'margin-left': '20px'})     
            ]),    
        ])
    ]),
    # Third column 
    dbc.Col([
        html.Div([
            html.H3('Score per Pillar', style={'text-align': 'center', 'margin-bottom': '10px'}),
            dcc.Graph(id='bar-chart')
        ])
    ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)