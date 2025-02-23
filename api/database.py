from supabase import Client, create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPEBASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

if not all([SUPEBASE_URL, SUPABASE_KEY, SUPABASE_JWT_SECRET]):
    raise ValueError("Please provide all the environment variables")

supabase: Client = create_client(SUPEBASE_URL, SUPABASE_KEY)
