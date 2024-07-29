from supabase_client import supabase

# Function to call the SQL function to create a user-specific table
def insert_user_table(user_email):
    
    # Prepare the data to be written
    record = {
        "user_email": user_email,
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
        print(f"Successfully inserted record for user {user_email}")
    else:
        print(f"Failed to insert record for user {user_email}: {response.error_message}")


def add_player(user_email, player_position, player_name):
    # Prepare the data to be written
    record = {
        player_position: player_name,
    }
    player_price = supabase.table("playervalues").select("price").match({"player": player_name}).execute().data[0]["price"]
    update_coins(user_email, player_price)
    response = supabase.table("user_teams").update(record).match({"user_email": user_email}).execute()
    if response.data:
        print(f"Successfully updated record for user {user_email}")
    else:
        print(f"Failed to update record for user {user_email}: {response.error_message}")


def remove_player(user_email, player_position, player_name ):
    # Prepare the data to be written
    record = {
        player_position: "",
    }
    player_price = supabase.table("playervalues").select("price").match({"player": player_name}).execute().data[0]["price"]
    update_coins(user_email, -player_price)
    response = supabase.table("user_teams").update(record).match({"user_email": user_email}).execute()
    if response.data:
        print(f"Successfully updated record for user {user_email}")
    else:
        print(f"Failed to update record for user {user_email}: {response.error_message}")


def update_coins(user_email, player_price):
    # Prepare the data to be written
    coins = supabase.table("user_teams").select("coins").match({"user_email": user_email}).execute().data[0]["coins"]
    record = {
        "coins": coins - player_price,
    }
    response = supabase.table("user_teams").update(record).match({"user_email": user_email}).execute()
    if response.data:
        print(f"Successfully updated record for user {user_email}")
    else:
        print(f"Failed to update record for user {user_email}: {response.error_message}")


def update_points(user_email, points):
    # Prepare the data to be written
    total_points = supabase.table("user_teams").select("total_points").match({"user_email": user_email}).execute().data[0]["total_points"]
    record = {
        "total_points": total_points + points,
    }
    response = supabase.table("user_teams").update(record).match({"user_email": user_email}).execute()
    if response.data:
        print(f"Successfully updated record for user {user_email}")
    else:
        print(f"Failed to update record for user {user_email}: {response.error_message}")


# # Test insert_user_table function
# insert_user_table("test@example.com")

# # Test add_player function
# add_player("test@example.com", "center", "Nikola Jokic")

# # Test remove_player function
# remove_player("test@example.com", "center", "Nikola Jokic")

# #test update_coins function
# update_points("test@example.com", 100)

