# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CHANGE THIS to your actual Postgres password
# Format: postgresql://username:password@localhost/databasename
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345678@localhost/speakflow"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to give access to the database in every API call
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()