import os
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join("config", "fda_api.env"))
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("FDA_API_KEY")
BASE_URL = os.getenv("FDA_BASE_URL")