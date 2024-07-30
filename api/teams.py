import sys
import os

# Add the parent directory to the system path in order to use config.supabase_client
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nba_api.stats.static import teams
from config.supabase_client import supabase

# Get all teams
nba_teams = teams.get_teams()

# Print team IDs
print(nba_teams)


for team in nba_teams:
    team_data = {
        'team_id': team['id'],
        'team_name': team['full_name'],
        'team_abbreviation': team['abbreviation'],
        'team_nickname': team['nickname'],
        'team_city': team['city'],
        'team_state': team['state'],
        'year_founded': team['year_founded']
    }
    supabase.table('teamdata').insert(team_data).execute()

print("All team data has been inserted into Supabase.")
