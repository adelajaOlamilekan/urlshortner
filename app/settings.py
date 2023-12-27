from dotenv import load_dotenv
import os
import argparse
import uvicorn 

load_dotenv()

parser = argparse.ArgumentParser(
        description="URL Shortening Server"
    )
parser.add_argument("--runstate", required=True, type=str, default="local")
args = parser.parse_args()

RUN_STATE = args.runstate



LOCAL_URL_ARGS_VALUE = os.getenv("LOCAL_URL_ARGS_VALUE")
LOCAL_DB_URL = os.getenv("LOCAL_DB_URL")
LIVE_DB_URL = os.getenv("LIVE_DB_URL")
LOCAL_API_BASE_URL = os.getenv("LOCAL_API_BASE_URL")
LIVE_API_BASE_URL = os.getenv("LIVE_API_BASE_URL")
LINK_SHORTENER_ENCODING_SCHEME = os.getenv("LINK_SHORTENER_ENCODING_SCHEME")

IS_LOCAL_INSTANCE = RUN_STATE == LOCAL_URL_ARGS_VALUE

DB_URL = LOCAL_DB_URL if IS_LOCAL_INSTANCE else LIVE_DB_URL
API_BASE_URL = LOCAL_API_BASE_URL if IS_LOCAL_INSTANCE else LIVE_API_BASE_URL



