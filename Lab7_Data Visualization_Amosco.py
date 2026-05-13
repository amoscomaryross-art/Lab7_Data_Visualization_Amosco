# Load & Preprocess
import numpy as np
import pandas as pd

dataset_path = r"C:\Users\YourName\Documents\Activity 7\spotify_top_1000_tracks.csv"  # ← Fix path

df = pd.read_csv(dataset_path, encoding="utf-8")

df['release_date']  = pd.to_datetime(df['release_date'], errors='coerce')
df['release_year']  = df['release_date'].dt.year
df['year']          = df['release_year']
df['decade']        = (df['release_year'] // 10) * 10

# Clean text
for col in ['track_name', 'artist', 'album']:
    if col in df.columns:
        df[col] = df[col].str.strip()

df['year'] = df['year'].fillna(0).astype(int)

# Tempo category
if 'tempo' in df.columns:
    df['tempo_category'] = pd.cut(df['tempo'],
                                   bins=[0, 100, 140, np.inf],
                                   labels=['Slow','Medium','Fast'],
                                   right=False)

df = df.drop_duplicates(subset=['track_name','artist'], keep='first')

print("✅ Dataset ready | Rows:", len(df))
print(df.head(3))