"""
Database Setup and Connection

"""

from sqlalchemy import(
    create_engine, URL
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import(
    DB_USER, DB_PASSWORD, DB_HOST,
    DB_TYPE, DB_NAME, DB_DRIVER,
    MYSQL, SQLITE, POSTGRESQL
)

if DB_TYPE in [MYSQL, POSTGRESQL]:
    db_url = URL.create(
        drivername = f"{DB_TYPE}+{DB_DRIVER}",
        username = DB_USER,
        password = DB_PASSWORD,
        host = DB_HOST,
        database = DB_NAME   
    )

else:
    db_url = f"{DB_TYPE}:///{DB_NAME}.db"

db_engine = create_engine(db_url)

# Create all Database Tables
Base = declarative_base()

# Create Database Session
Database_Session = sessionmaker(bind=db_engine)

def create_database_table():
    """"
    Creates non-existent tables in the database

    Args
        None
    
    Return
        None

    """

    Base.metadata.create_all(db_engine)

# Connect to the Database Session

def get_db_session() -> Database_Session:
    """
    Gets a database session

    Creates the database schema if it doesn't exist and opens
    a new database session. The session is closed before returning. 

    Args 
        None
    
    Return:
        Database_Session: A database session
    """

    create_database_table()
    db_session = Database_Session()

    try:
        yield db_session
    
    finally:
        db_session.close()