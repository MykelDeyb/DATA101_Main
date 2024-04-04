import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import geopandas as gpd
import numpy as np
from openpyxl import load_workbook
from pathlib import Path
import plotly.graph_objects as go
import numpy as np

dataset_folder = Path('Datasets/')
workbook = load_workbook(dataset_folder / 'InteractiveMap_Data/InteractiveMap_Profile.xlsx')

all_years = list(range(2014, 2024))

# Map
file_paths = [
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-bicolregionregionv.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-autonomousregionofmuslimmindanaoarmm.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-cagayanvalleyregionii.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-calabarzonregioniva.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-caragaregionxiii.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-centralluzonregioniii.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-centralvisayasregionvii.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-cordilleraadministrativeregioncar.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-davaoregionregionxi.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-easternvisayasregionviii.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-ilocosregionregioni.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-metropolitanmanila.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-mimaroparegionivb.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-northernmindanaoregionx.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-soccsksargenregionxii.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-westernvisayasregionvi.json",
    "/Users/kylacansana/Downloads/Province JSON/provinces-region-zamboangapeninsularegionix.json"
]

# Read each file and append to a list
ph_list = [gpd.read_file(file) for file in file_paths]

# Combine all GeoDataFrames in the list into a single GeoDataFrame
ph = gpd.GeoDataFrame(pd.concat(ph_list, ignore_index=True), crs=ph_list[0].crs)
#ph = ph.to_crs(epsg=32651)
p_score = pd.read_csv(dataset_folder / 'Province_Data/Overall Score.csv', encoding='latin1')
ph.loc[ph['PROVINCE'] == 'Agusan del Norte', 'PROVINCE'] = 'Agusan Del Norte'
ph.loc[ph['PROVINCE'] == 'Agusan del Sur', 'PROVINCE'] = 'Agusan Del Sur'
ph.loc[ph['PROVINCE'] == 'Batangas', 'PROVINCE'] = 'Batangas Province'
ph.loc[ph['PROVINCE'] == 'Biliran', 'PROVINCE'] = 'Biliran Province'
ph.loc[ph['PROVINCE'] == 'Cavite', 'PROVINCE'] = 'Cavite Province'
ph.loc[ph['PROVINCE'] == 'Cebu', 'PROVINCE'] = 'Cebu Province'
ph.loc[ph['PROVINCE'] == 'North Cotabato', 'PROVINCE'] = 'Cotabato (North Cotabato)'
ph.loc[ph['PROVINCE'] == 'Davao de Oro', 'PROVINCE'] = 'Davao De Oro'
ph.loc[ph['PROVINCE'] == 'Davao del Norte', 'PROVINCE'] = 'Davao Del Norte'
ph.loc[ph['PROVINCE'] == 'Davao del Sur', 'PROVINCE'] = 'Davao Del Sur'
ph.loc[ph['PROVINCE'] == 'Iloilo', 'PROVINCE'] = 'Iloilo Province'
ph.loc[ph['PROVINCE'] == 'Lanao del Norte', 'PROVINCE'] = 'Lanao Del Norte'
ph.loc[ph['PROVINCE'] == 'Lanao del Sur', 'PROVINCE'] = 'Lanao Del Sur'
ph.loc[ph['PROVINCE'] == 'Leyte', 'PROVINCE'] = 'Leyte Province'
ph.loc[ph['PROVINCE'] == 'Masbate', 'PROVINCE'] = 'Masbate Province'
ph.loc[ph['PROVINCE'] == 'Romblon', 'PROVINCE'] = 'Romblon Province'
ph.loc[ph['PROVINCE'] == 'Samar', 'PROVINCE'] = 'Samar (Western Samar)'
ph.loc[ph['PROVINCE'] == 'Siquijor', 'PROVINCE'] = 'Siquijor Province'
ph.loc[ph['PROVINCE'] == 'Sorsogon', 'PROVINCE'] = 'Sorsogon Province'
ph.loc[ph['PROVINCE'] == 'Surigao del Norte', 'PROVINCE'] = 'Surigao Del Norte'
ph.loc[ph['PROVINCE'] == 'Surigao del Sur', 'PROVINCE'] = 'Surigao Del Sur'
ph.loc[ph['PROVINCE'] == 'Tarlac', 'PROVINCE'] = 'Tarlac Province'
ph.loc[ph['PROVINCE'] == 'Zamboanga del Norte', 'PROVINCE'] = 'Zamboanga Del Norte'
ph.loc[ph['PROVINCE'] == 'Zamboanga del Sur', 'PROVINCE'] = 'Zamboanga Del Sur'
#ph.loc[ph['PROVINCE'] == 'Maguindanao del Norte', 'PROVINCE'] = 'Maguindanao'
#ph.loc[ph['PROVINCE'] == 'Maguindanao del Sur', 'PROVINCE'] = 'Maguindanao'
ph.loc[ph['PROVINCE'] == 'Metropolitan Manila', 'PROVINCE'] = 'Metro Manila'
p_choro = pd.merge(ph, p_score,  left_on='PROVINCE', right_on='PROVINCE / LGU', how='left', indicator=True)

# print(p_choro)

initial_column_values = p_choro.set_index('PROVINCE').get('2023', pd.Series(index=p_choro.index, dtype=float))
initial_column_values = initial_column_values.replace('-', np.nan).astype(float).fillna(0).astype(int)

# print(initial_column_values)

numeric_values = initial_column_values.dropna()
colors = numeric_values.values

# print(colors)

print(ph.loc[ph['PROVINCE'] == 'Cebu Province', 'geometry'].get_coordinates().iloc[0]['x'])