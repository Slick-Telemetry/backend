# Built-in
import os

# External
import fastf1
from dotenv import dotenv_values
from fastapi.security import HTTPBearer
from fastf1.ergast import Ergast


__version__ = "0.7.0"


# Load environment variables from .env file
if os.path.isfile(".env"):
    # Load environment variables from .env file for local development
    config = dotenv_values(".env")
else:
    # Load environment variables from Heroku's environment variable system for production
    config = dict(os.environ)
# FastF1 configuration
fastf1.set_log_level("WARNING")
fastf1.Cache.set_disabled()
# Ergast configuration
ergast = Ergast(result_type="raw", auto_cast=True)
# Cors Middleware
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    config["FRONTEND_DEV_URL"],
    config["FRONTEND_STAGING_URL"],
    config["FRONTEND_PROD_URL"],
]
# Others
favicon_path = "favicon.ico"
# Security
security = HTTPBearer()
