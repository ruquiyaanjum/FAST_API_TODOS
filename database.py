"""
connection to MySQL database
"""
import os  # Interact with OS
from dotenv import load_dotenv  # Load secret info
from sqlalchemy import create_engine, MetaData  # Connect to DB
from sqlalchemy.orm import sessionmaker  # Create DB session
from sqlalchemy.orm import declarative_base  # Create table models

load_dotenv()  # Load .env file

database_url = os.getenv("DATABASE_URL")  # Get DB URL

engine = create_engine(database_url)  # Creates the connection to the database

metadata = MetaData()  # Store DB structure

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Creates sessionmaker to interact with DB

Base = declarative_base()  # Create table
