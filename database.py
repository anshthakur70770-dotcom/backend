from supabase import Client,create_client
from  dotenv import load_dotenv
import os
load_dotenv()
url = os.getenv("SUPABASEURL")
key = os.getenv("SUPABASEKEY")

if not url or not key :
    raise ValueError("creadients are wrong")
else :
    supabase : Client = create_client(url,key)
    print("sussess")
    