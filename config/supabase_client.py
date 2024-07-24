from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client


url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

supabase = create_client(url, key)

#  EXAMPLE to get all data from todos table
# data = supabase.table('todos').select('*').execute()
# print(data)


# EXAMPLE to insert data into todos table
# data = supabase.table('todos').insert({"name":"Todo 2"}).execute()
# data = supabase.table('todos').select("*").execute()
# print(data)

# EXAMPLE to update data in todos table
# data = supabase.table('todos').update({"name":"Todo 3"}).eq('id', 1).execute()
# data = supabase.table('todos').select("*").execute()