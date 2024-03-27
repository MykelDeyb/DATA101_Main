import pandas as pd

distance_path = r'C:\Users\Cara\Downloads\Distance Provinces.csv'
overall_score_path = r'C:\Users\Cara\Downloads\Overall Score (6).csv'
provinces_path = 'provinces.csv'

distance_df = pd.read_csv(distance_path)
overall_score_df = pd.read_csv(overall_score_path)

merged_df = pd.merge(distance_df, overall_score_df, on="Province")

merged_df.to_csv(provinces_path, index=False)

