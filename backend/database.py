from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pymongo import MongoClient
from backend.config import DATABASE_URL, MONGO_URL, MONGO_DB

# PostgreSQL
engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# MongoDB
mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client[MONGO_DB]
tasks_collection = mongo_db["tasks"]