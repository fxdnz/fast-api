import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using environment variable for database URL
database_url = "postgresql://fastapi_user:yu4JpwGYTiIDdlRLsOmEUA4E04sug3Lr@dpg-d0pd0vemcj7s73e0h0ug-a.singapore-postgres.render.com/fastapi_ambotdb"

# Creating the engine to interact with PostgreSQL
engine = create_engine(database_url, echo=True)
# Creating a session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base class to create tables
Base = declarative_base()