from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import User 

setting=User()



SQLALCHEMY_DATABASE_URL = f"postgresql://{setting.DATABASE_USERNAME}:{setting.DATABASE_PASSWORD}@{setting.DATABASE_HOSTNAME}:{setting.DATABASE_PORT}/{setting.DATABASE_NAME}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()