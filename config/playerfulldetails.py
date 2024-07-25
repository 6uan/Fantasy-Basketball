# 50-60ish players are failing to get inserted

import pandas as pd
from supabase_client import supabase

# Read the CSV file into a DataFrame
df = pd.read_csv('../data/output_data.csv')

# Convert column names to lowercase
df.columns = [col.lower() for col in df.columns]

# Replace NaN values with None
df = df.where(pd.notna(df), None)

# Convert DataFrame to list of dictionaries
data = df.to_dict(orient='records')

# Insert data into Supabase
for idx, record in enumerate(data):
    try:
        response = supabase.table('players').insert(record).execute()
        if response.status_code != 201:
            print(f"Error inserting record {idx}: {response.json()}")
    except Exception as e:
        print(f"Exception at record {idx}: {e}")
        print(f"Record causing issue: {record}")

print("Data insertion complete.")
