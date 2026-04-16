from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

try:
    client = MongoClient(os.getenv("MONGO_URL"))
    db = client[os.getenv("MONGO_DB")]

    # Test operation
    db.test.insert_one({"test": "connection"})

    print("✅ Connected to MongoDB Atlas successfully!")

except Exception as e:
    print("❌ Connection failed:", e)