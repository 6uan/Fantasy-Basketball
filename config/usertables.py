from config.supabase_client import supabase

# Function to call the SQL function to create a user-specific table
def insert_user_table(uid):
    
    # Prepare the data to be written
    record = {
        "uid": uid,
        "total_points": 0,
        "coins": 450,
        "center": "",
        "point_guard": "",
        "shooting_guard": "",
        "power_forward": "",
        "small_forward": "",
    }
    response = supabase.table("user_teams").upsert(record).execute()
    if response.data:
        print(f"Successfully inserted record for user {uid}")
    else:
        print(f"Failed to insert record for user {uid}: {response.error_message}")


def add_player(uid, player_position, person_id):
    # Prepare the data to be written
    record = {
        player_position: person_id,
    }
    player_price = supabase.table("playervalues").select("price").match({"person_id": person_id}).execute().data[0]["price"]
    update_coins(uid, player_price)
    response = supabase.table("user_teams").update(record).match({"uid": uid}).execute()
    if response.data:
        print(f"Successfully updated record for user {uid}")
    else:
        print(f"Failed to update record for user {uid}: {response.error_message}")


def remove_player(uid, player_position, person_id ):
    # Prepare the data to be written
    record = {
        player_position: "",
    }
    player_price = supabase.table("playervalues").select("price").match({"person_id": person_id}).execute().data[0]["price"]
    update_coins(uid, -player_price)
    response = supabase.table("user_teams").update(record).match({"uid": uid}).execute()
    if response.data:
        print(f"Successfully updated record for user {uid}")
    else:
        print(f"Failed to update record for user {uid}: {response.error_message}")


def update_coins(uid, player_price):
    # Prepare the data to be written
    coins = supabase.table("user_teams").select("coins").match({"uid": uid}).execute().data[0]["coins"]
    record = {
        "coins": coins - player_price,
    }
    response = supabase.table("user_teams").update(record).match({"uid": uid}).execute()
    if response.data:
        print(f"Successfully updated record for user {uid}")
    else:
        print(f"Failed to update record for user {uid}: {response.error_message}")


def update_points(uid, points):
    # Prepare the data to be written
    total_points = supabase.table("user_teams").select("total_points").match({"uid": uid}).execute().data[0]["total_points"]
    record = {
        "total_points": total_points + points,
    }
    response = supabase.table("user_teams").update(record).match({"uid": uid}).execute()
    if response.data:
        print(f"Successfully updated record for user {uid}")
    else:
        print(f"Failed to update record for user {uid}: {response.error_message}")

def get_user_team(uid):
    response = supabase.table('user_teams').select('*').eq('uid', uid).execute()
    if response.data:
        print(f"Successfully grabbed record for user {uid}")
    else:
        print(f"Failed to grab record for user {uid}: {response.error_message}")
    return response.data[0]


# # Test insert_user_table function
# insert_user_table("34e38f90-1947-4e4d-aa64-28e96ae978df")

# # Test add_player function
# add_player("34e38f90-1947-4e4d-aa64-28e96ae978df", "center", 203999)

# # Test remove_player function
# remove_player("5062d069-7159-4825-9499-587db7788618", "center", 203999)



