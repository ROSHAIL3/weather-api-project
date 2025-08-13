# config.py
import os
from dataclasses import dataclass
from dotenv import load_dotenv  # ←←← Added

# Load environment variables from .env file
load_dotenv()  # ←←← This loads the .env file

@dataclass
class Config:
    """App configuration"""
    API_KEY: str = os.getenv("OPENWEATHER_API_KEY")
    BASE_URL: str = "http://api.openweathermap.org/data/2.5/weather"
    GEO_URL: str = "http://api.openweathermap.org/geo/1.0/direct"

    def validate(self):
        if not self.API_KEY:
            raise ValueError(
                "OPENWEATHER_API_KEY not found. "
                "Please set it in the .env file."
            )