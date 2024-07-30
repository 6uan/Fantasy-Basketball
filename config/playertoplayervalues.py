from supabase_client import supabase

# Fetch data from players table
players_response = supabase.table('players').select('*').execute()
players_data = players_response.data

# Fetch data from playervalues table
playervalues_response = supabase.table('playervalues_original').select('*').execute()
playervalues_data = playervalues_response.data

# Convert players data to a dictionary for quick lookup
players_dict = {player['display_first_last']: player for player in players_data}

# Iterate through playervalues data and update records
for item in playervalues_data:
    player_name = item['player']
    if player_name in players_dict:
        player_info = players_dict[player_name]
        player_id = player_info['person_id']
        position = player_info['position']
        team_id = player_info['team_id']

        # Prepare the data to be written
        record = {
            "person_id": player_id,
            "overall": item['overall'],
            "price": item['price'],
            "player": player_name,
            "team": item['team'],
            "position": position,
            "team_id": team_id
        }

        response = supabase.table("playervalues").update(record).eq("player", player_name).execute()
        if response.data:
            print(f"Successfully inserted record for player {player_name}")
        else:
            print(f"Failed to insert record for player {player_name}: {response.error_message}")
    else:
        print(f"No matching player found in 'players' table for {player_name}")

print("Data instertion complete.")
