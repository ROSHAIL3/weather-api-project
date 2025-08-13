# main.py
from weather_api import WeatherAPI

def main():
    print("🌍 Simple Weather App\n")
    
    # You can change this city/country
    city = input("Enter city name (e.g., London): ").strip()
    if not city:
        city = "London"
    
    country = input("Enter country code (e.g., GB, US, optional): ").strip()
    if not country:
        country = None

    try:
        api = WeatherAPI()
        print(f"\nFetching weather for {city}...\n")
        weather = api.get_weather(city, country)
        print(weather)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()