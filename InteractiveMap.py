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

lgu_data = [row[0].value for row in lgu_sheet.iter_rows(min_row=2, max_col=1)]
category_data = [row[1].value for row in lgu_sheet.iter_rows(min_row=2, max_col=2)]
province_data = [row[3].value for row in lgu_sheet.iter_rows(min_row=2, max_col=4)]
revenue_data = [row[4].value for row in lgu_sheet.iter_rows(min_row=2, max_col=5)]
lgu_options = [{'label': lgu_name, 'value': lgu_name} for lgu_name in lgu_data if lgu_name is not None]

def get_pillar_description(selected_pillar):
    pillar_descriptions = {
        'Resiliency': 'Applies to the capacity of a locality to build systems that can absorb change and disturbance and being able to adapt to such changes. It spans frameworks that bind LGUs and their constituents to prepare for possible shocks and stresses; budgeting for disaster risk reduction; hazard/risk identification mechanisms; resilience-related infrastructure; and resilience-related mechanisms.',
        'Government Efficiency': 'Refers to the quality and reliability of government services and government support for effective and sustainable productive expansion. This factor looks at government as an institution that is generally not corrupt; able to protect and enforce contracts; apply moderate and reasonable taxation and is able to regulate proactively.',
        'Innovation': 'Refers to the ability of a locality to harness its creative potential to improve or sustain current levels of productivity. It hinges mainly on the development of creative capital which are human resources, research capabilities, and networking capacities..',
        'Economic Dynamism': 'Refers to stable expansion of businesses and industries and higher employment. Matches output and productivity of the local economy with the local resources. Localities are centers of economic activities, and due to this, business expansion and job creation are easily observable in local settings.',
        'Infrastructure': 'Pertains to the physical assets that connect, expand, and sustain a locality and its surroundings to enable provision of goods and services. It involves basic inputs of production such as energy, water; interconnection of production such as transportation, roads and communications; sustenance of production such as waste, disaster preparedness, environmental sustainability; and human capital formation infrastructure.'
    }
    return pillar_descriptions.get(selected_pillar, 'No description available')

def get_lgu_province(selected_lgu):
    try:
        index = lgu_data.index(selected_lgu)
        return province_data[index]
    except ValueError:
        return 'No data available'

def get_lgu_category(selected_lgu):
    try:
        index = lgu_data.index(selected_lgu)
        return category_data[index]
    except ValueError:
        return 'No data available'

def get_lgu_revenue(selected_lgu):
    try:
        index = lgu_data.index(selected_lgu)
        return revenue_data[index]
    except ValueError:
        return 'No data available'

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
                options=lgu_options,
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
                html.Div(id='pillar-description')
                ])
            ], style={'margin-left': '20px'}),
            # LGU Profile
            dbc.Row([
                dbc.Col([
                html.Label('Province'),
                html.Div(id='province-label')
                ]),
                dbc.Col([
                html.Label('Category'),
                html.Div(id='category-label')
                ]),
                dbc.Col([
                html.Label('Revenue'),
                html.Div(id='revenue-label')
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

@app.callback(
    [
        Output('pillar-description', 'children'),
        Output('province-label', 'children'),
        Output('category-label', 'children'),
        Output('revenue-label', 'children'),
    ],
    [
        Input('lgu-dropdown', 'value'),
        Input('pillar-dropdown', 'value')
    ]
)
def update_labels(selected_lgu, selected_pillar):
    if selected_lgu and selected_pillar:
        pillar_description = get_pillar_description(selected_pillar)
        lgu_province = get_lgu_province(selected_lgu)
        lgu_category = get_lgu_category(selected_lgu)
        lgu_revenue = get_lgu_revenue(selected_lgu)

        return pillar_description, lgu_province, lgu_category, lgu_revenue
    else:
        return '', '', '', ''

# Bar Chart
@app.callback(
    Output('bar-chart', 'figure'),
    Input('lgu-dropdown', 'value')
)
def update_bar_chart(selected_lgu):
    if not selected_lgu:
        return {}

    lgu_index = lgu_data.index(selected_lgu) + 2
    lgu_data_row = list(lgu_sheet.iter_rows(min_row=lgu_index, max_row=lgu_index, min_col=6, max_col=10, values_only=True))[0]
    pillars = ['Resiliency', 'Government Efficiency', 'Innovation', 'Economic Dynamism', 'Infrastructure']

    fig = px.bar(
        x=pillars,
        y=lgu_data_row,
        labels={'x': 'Pillar', 'y': 'Score'},
        title=f'Scores per Pillar for {selected_lgu}'
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

