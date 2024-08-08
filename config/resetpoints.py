from config.supabase_client import supabase

def resetpoints():
    response = supabase.table("playervalues").update({"total_points": 0}).neq("person_id", 0).execute()
    if response.data:
        print(f"Successfully reset total points for all players")
    
    response = supabase.table("playervalues").update({"points_current_matchday": 0}).neq("person_id", 0).execute()
    if response.data:
        print(f"Successfully reset current matchday points for all players")
    
    response = supabase.table("user_teams").update({"points_matchday": 0}).neq("uid", 0).execute()
    if response.data:
        print(f"Successfully reset matchday points for all users")
    
    response = supabase.table("user_teams").update({"total_points": 0}).neq("uid", 0).execute()
    if response.data:
        print(f"Successfully reset total points for all users")

resetpoints()
