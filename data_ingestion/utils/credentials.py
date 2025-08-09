import os
from dotenv import load_dotenv
from pathlib import Path

# Locate and load the .env file
env_path = Path(__file__).resolve().parent / "api_keys.env"
if not env_path.exists():
    raise FileNotFoundError(f"[ERROR] .env file not found at {env_path}")
else:
    print(f"[DEBUG] .env path: {env_path}")

load_dotenv(dotenv_path=env_path)

def load_api_config(service: str) -> dict:
    key = os.getenv(f"{service.upper()}_API_KEY")
    if service.lower() == "cms_api":
        url = os.getenv(f"{service.upper()}_URL")
        # Only require URL for CMS API
        if not url: 
            print(f"[WARN] Missing API URL for '{service}'. Check environment file at {env_path}")
        return {"base_url": url}  # Removed api_key for cms_api
    else:
        url = os.getenv(f"{service.upper()}_BASE_URL")
        if not key or not url:
            print(f"[WARN] Missing API config for '{service}'. Check environment file at {env_path}")
        return {"api_key": key, "base_url": url}

print("CMS_API_URL:", os.getenv("CMS_API_URL"))