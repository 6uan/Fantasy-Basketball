import pandas as pd
from supabase_client import supabase

# Read the CSV file into a DataFrame
df = pd.read_csv('../data/players_2022_2023.csv')

# Convert column names to lowercase
df.columns = [col.lower() for col in df.columns]

df = df.where(pd.notna(df), None)

# Convert DataFrame to list of dictionaries
data = df.to_dict(orient='records')

# Insert data into Supabase
for record in data:
    response = supabase.table('playerdata').insert(record).execute()