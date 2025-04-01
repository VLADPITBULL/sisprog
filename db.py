from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Измени параметры на свои!
user = "postgres"
password = "yourpassword"
host = "localhost"
port = "5432"
db = "your_db_name"

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
