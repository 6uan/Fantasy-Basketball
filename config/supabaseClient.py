import os
from supabase import create_client, Client

url: str = os.environ.get("https://qzdtfqxubskpxfdqqmcs.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF6ZHRmcXh1YnNrcHhmZHFxbWNzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjEzNTMwMTgsImV4cCI6MjAzNjkyOTAxOH0.ZcwpA0zQMKKI9NXKu-70e_BbdR6_SDiRE_34Mlx2YRQ")
supabase: Client = create_client(url, key)