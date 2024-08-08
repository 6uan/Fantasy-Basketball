from config.supabase_client import supabase

def create_overall_leaderboard(user_points):
    leaderboard = {uid: points for uid, points in user_points.items()}
    sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))
    return sorted_leaderboard

def create_matchday_leaderboard(user_points):
    leaderboard = {uid: points for uid, points in user_points.items()}
    sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))
    return sorted_leaderboard

def fetch_user_points(usertables):
    user_points = {}
    for uid in usertables:
        response = supabase.table("user_teams").select("total_points").match({"uid": uid}).execute()
        if response.data:
            user_points[uid] = response.data[0].get("total_points", 0)
    return user_points

def fetch_matchday_points(usertables):
    user_points = {}
    for uid in usertables:
        response = supabase.table("user_teams").select("points_matchday").match({"uid": uid}).execute()
        if response.data:
            user_points[uid] = response.data[0].get("points_matchday", 0)
    return user_points

def fetch_usertables():
    response = supabase.table("user_teams").select("uid").execute()
    if response.data:
        usertables = [user["uid"] for user in response.data]
        return usertables

def overall_leaderboard():
    usertables = fetch_usertables()
    if usertables:
        total_points = fetch_user_points(usertables)
        overall_leaderboard = create_overall_leaderboard(total_points)
        return overall_leaderboard
    return None

def matchday_leaderboard():
    usertables = fetch_usertables()
    if usertables:
        matchday_points = fetch_matchday_points(usertables)
        matchday_leaderboard = create_matchday_leaderboard(matchday_points)
        return matchday_leaderboard
    return None
