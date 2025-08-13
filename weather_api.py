# weather_api.py
import requests
from datetime import datetime
from dataclasses import dataclass
from config import Config

@dataclass
class Location:
    name: str
    latitude: float
    longitude: float
    country: str
    state: str = None

@dataclass
class WeatherData:
    location: Location
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
    description: str
    wind_speed: float
    wind_direction: int
    visibility: int
    timestamp: datetime

    @property
    def temp_celsius(self) -> float:
        return self.temperature - 273.15

    @property
    def temp_fahrenheit(self) -> float:
        return (self.temperature - 273.15) * 9/5 + 32

    def __str__(self):
        return f"""
🌤️  Current Weather in {self.location.name}, {self.location.country}
----------------------------------------
🌡️  Temperature:     {self.temp_celsius:.1f}°C ({self.temp_fahrenheit:.1f}°F)
🧍‍♂️  Feels like:      {self.feels_like - 273.15:.1f}°C
💧 Humidity:         {self.humidity}%
🔽 Pressure:         {self.pressure} hPa
🌬️  Wind:            {self.wind_speed} m/s from {self.wind_direction}°
👀 Visibility:       {self.visibility} m
⛅ Condition:        {self.description.title()}
🕒 Updated:         {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        """.strip()

class WeatherAPI:
    def __init__(self):
        self.config = Config()
        self.config.validate()

    def _get(self, url: str, params: dict) -> dict:
        """Make HTTP GET request"""
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise Exception("Request timed out")
        except requests.exceptions.ConnectionError:
            raise Exception("Failed to connect to the server")
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                raise Exception("City not found")
            else:
                raise Exception(f"HTTP error: {e}")

    def get_coordinates(self, city: str, country: str = None) -> Location:
        """Convert city name to coordinates"""
        params = {
            "q": f"{city},{country}" if country else city,
            "limit": 1,
            "appid": self.config.API_KEY
        }
        url = self.config.GEO_URL
        data = self._get(url, params)

        if not data:  # ✅ Fixed: now checks if data is empty
            raise Exception(f"City '{city}' not found")

        loc = data[0]
        return Location(
            name=loc.get("name", city),
            latitude=loc["lat"],
            longitude=loc["lon"],
            country=loc["country"],
            state=loc.get("state")
        )

    def get_weather(self, city: str, country: str = None) -> WeatherData:
        """Get current weather for a city"""
        location = self.get_coordinates(city, country)

        params = {
            "lat": location.latitude,
            "lon": location.longitude,
            "appid": self.config.API_KEY
        }
        data = self._get(self.config.BASE_URL, params)

        return WeatherData(
            location=location,
            temperature=data["main"]["temp"],
            feels_like=data["main"]["feels_like"],
            humidity=data["main"]["humidity"],
            pressure=data["main"]["pressure"],
            description=data["weather"][0]["description"],
            wind_speed=data.get("wind", {}).get("speed", 0),
            wind_direction=data.get("wind", {}).get("deg", 0),
            visibility=data.get("visibility", 0),
            timestamp=datetime.fromtimestamp(data["dt"])
        )