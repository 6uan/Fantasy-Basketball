import json
import os
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

with open('../nba2k-player-ratings/data/league.json', 'r') as file:
    data = json.load(file)

def write_to_table(data):
    player_id = 1
    for item in data:
        player_name = item['name']
        team = item['team']
        overall = item['overallAttribute']
        price = overall * 1.25
        
        # Prepare the data to be written
        record = {
            "id": player_id,
            "overall": overall,
            "price": price,
            "player": player_name,
            "team": team
        }

        response = supabase.table("playervalues").update(record).eq("id",player_id).execute()
        if response.data:
            print(f"Successfully inserted record for player {player_name}")
        else:
            print(f"Failed to insert record for player {player_name}: {response.error_message}")
        
        player_id += 1
    
write_to_table(data)
    