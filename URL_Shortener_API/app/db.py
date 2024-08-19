from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# URL parameters

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"

# creating the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# db function to create the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()