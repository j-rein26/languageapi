from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_PWD = os.getenv('DATABASE_PWD')

URL_DATABASE = f'postgresql://postgress:{DATABASE_PWD}@localhost:5432/turkishlanguage'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()