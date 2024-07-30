import sys
import os

# Add the parent directory to the system path in order to use config.supabase_client
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.supabase_client import supabase

# Fetch the team data
response = supabase.table('teamdata').select('*').execute()

# Iterate through the team data and update the logo URLs
for team in response.data:
    team_id = team['team_id']
    logo_url = f"https://cdn.nba.com/logos/nba/{team_id}/primary/L/logo.svg"

    # Update the team data with the logo URL
    supabase.table('teamdata').update({'team_logo': logo_url}).eq('team_id', team_id).execute()

print("All team logos have been updated in Supabase.")
