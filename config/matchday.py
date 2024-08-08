from config.supabase_client import supabase
from config.usertables import update_points, update_matchday_points

def fetch_user_teams():
    try:
        response = supabase.table("user_teams").select("*").execute()
        if response.data:
            print(f"Fetched {len(response.data)} records from user_teams")
            return response.data
        else:
            print(f"Failed to fetch user teams: {response.error_message}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def update_player_points(person_id, points, user_teams):
    response = supabase.table('playervalues').select('total_points').eq("person_id", person_id).execute()
    if response.data:
        total_points = response.data[0]["total_points"]
        if total_points is None:
            total_points = 0
        response = supabase.table("playervalues").update({"total_points": total_points + points}).eq("person_id", person_id).execute()
        response = supabase.table("playervalues").update({"points_current_matchday": points}).eq("person_id", person_id).execute()
        for user_team in user_teams:
            user_id = user_team['uid']
            team_players = [
                user_team['center'],
                user_team['center_forward'],
                user_team['guard'],
                user_team['forward_center'],
                user_team['forward'],
                user_team['guard_forward']
            ]
            if person_id in team_players:
                update_points(user_id, points)

def update_current_matchday(user_teams):
    for user_team in user_teams:
        user_id = user_team['uid']
        team_players = [
            user_team['center'],
            user_team['center_forward'],
            user_team['guard'],
            user_team['forward_center'],
            user_team['forward'],
            user_team['guard_forward']
        ]
        matchday_points = 0 
        for person_id in team_players:
            if person_id:  # Check if person_id is valid (not None or empty)
                response = supabase.table("playervalues").select("points_current_matchday").eq("person_id", person_id).execute()
                if response.data and response.data[0]["points_current_matchday"] is not None:
                    matchday_points += response.data[0]["points_current_matchday"]
                else:
                    matchday_points += 0
        update_matchday_points(user_id, matchday_points)


# Function to fetch game data from the database
def fetch_game_data():
    try:
        response = supabase.table("boxscores").select("*").execute()
        if response.data:
            return response.data
        else:
            print(f"Failed to fetch game data: {response.data}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Process each game and update points
def process_games(matchday):
    data = fetch_game_data()
    user_teams = fetch_user_teams()
    print(len(data))
    games = list(set([game['GAME_ID'] for game in data]))
    print(len(games))
    games_for_matchday = games[(matchday - 1) * 15: matchday * 15]  # Only process 15 games for the current matchday
    print(len(games_for_matchday))
    for game_id in games_for_matchday:
        game_data = [game for game in data if game['GAME_ID'] == game_id]

        # Update player points for the game
        for row in game_data:
            player_name = row["PLAYER_NAME"]
            person_id = row['PLAYER_ID']
            points = 0
            if row["PTS"]:
                points += row['PTS']
            if row["REB"]:
                points += row['REB'] * 1.2
            if row["AST"]:
                points += row['AST'] * 1.5
            if row["MIN"]:
                if float(row['MIN'][0:5]) >= 30:
                    points += 10
            print(f"{player_name} scored {points} points")
            update_player_points(person_id, points, user_teams)

    update_current_matchday(user_teams)
