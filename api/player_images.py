import sys
import os
# Add the parent directory to the system path in order to use config.supabase_client
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.supabase_client import supabase
# Fetch the team data
response = supabase.table('playervalues').select('*').execute()
# Iterate through the team data and update the logo URLs
for person in response.data:
    person_id = person['person_id']
    person_url = f"https://cdn.nba.com/headshots/nba/latest/1040x760/{person_id}.png"
    # Update the team data with the logo URL
    supabase.table('playervalues').update({'person_picture': person_url}).eq('person_id', person_id).execute()
print("All player picture have been updated in Supabase.")