from dotenv import load_dotenv
load_dotenv()
import os

"""
CONSTANTS USED IN PROJECT
"""
MYSQL = "mysql"
SQLITE = "sqlite"
POSTGRESQL = "postgresql"
LINK_SHORTENER_ENCODING_SCHEME = "utf-8"
BACEKEND_PORT = 8000

"""
DATABASE SETTINGS VARIABLE
"""
LOCAL_DB_USER = "fastapi_user"
LOCAL_DB_PASSWORD = ""
LOCAL_DB_HOST= "localhost"
LOCAL_DB_PORT  = 3306
LOCAL_DB_NAME = "url_shortner"
DB_TYPE = MYSQL

"""
LIVE DATABASE CREDENTIALS
"""
LIVE_DB_USER = os.getenv("LIVE_DB_USER")
LIVE_DB_PASSWORD = os.getenv("LIVE_DB_PASSWORD")
LIVE_DB_HOST= os.getenv("LIVE_DB_HOST")
LIVE_DB_PORT  = os.getenv("LIVE_DB_PORT")
LIVE_DB_NAME = os.getenv("LIVE_DB_NAME")
LIVE_DB_DRIVER = os.getenv("LIVE_DB_DRIVER")
LIVE_BASE_URL = os.getenv("LIVE_BASE_URL")