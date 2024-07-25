import os
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client, Client

# Load environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Create Supabase client
supabase: Client = create_client(url, key)

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



