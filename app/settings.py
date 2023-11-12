from dotenv import load_dotenv
load_dotenv()

"""
DATABASE SETTINGS VARIABLE
"""

DB_USER = "fastapi_user"
DB_PASSWORD = ""
DB_HOST= "localhost"
DB_PORT  = 3306
DB_NAME = "url_shortner"
DB_TYPE = "sqlite"
DB_DRIVER = "driver"

"""
CONSTANTS USED IN PROJECT

"""
MYSQL = "mysql"
SQLITE = "sqlite"
POSTGRESQL = "postgresql"
LINK_SHORTENER_ENCODING_SCHEME = "utf-8"
BACEKEND_PORT = 8000
LIVE_BASE_URL = "https://kokuru.onrender.com"