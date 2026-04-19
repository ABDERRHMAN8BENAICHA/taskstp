import os
from dotenv import load_dotenv

# 🔥 لازم يكون في الأعلى
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pymongo import MongoClient

# ✅ اقرأ المتغيرات بعد load_dotenv
DATABASE_URL = os.getenv("DATABASE_URL")
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")

# ------------------ PostgreSQL ------------------

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # 🔥 يحل مشكلة SSL closed
    pool_recycle=300
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ------------------ MongoDB ------------------

mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client[MONGO_DB]
tasks_collection = mongo_db["tasks"]