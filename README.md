

```markdown
# 🌤️ Weather API Project

A simple Python weather app that fetches current weather data from [OpenWeatherMap API](https://openweathermap.org/api). Built with clean code, error handling, and easy setup.


---

## 🚀 Features

- Get real-time weather for any city
- Displays temperature, humidity, wind, and more
- Clean, readable output with emojis
- Input support for city and country
- Secure API key handling using `.env` file

---

## 📦 Prerequisites

Before you begin, make sure you have:

- [Python 3.7 or higher](https://www.python.org/downloads/)
- `pip` (Python package installer)
- Internet connection

---

## 🔧 Setup Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/weather-api-project.git
cd weather-api-project
```

> Or download and extract the ZIP file.

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `requests` – for HTTP calls
- `python-dotenv` – to load secure environment variables

---

### 3. Get Your Own Free API Key

⚠️ **You MUST use your own API key.**  
The project will NOT work without it.

1. Go to: [https://openweathermap.org/api](https://openweathermap.org/api)
2. Sign up for a **free account**
3. Navigate to: [https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)
4. Copy your **API key** (it looks like `a1b2c3d4e5f67890a1b2c3d4e5f67890`)

> 🔐 Never share your API key. Never commit it to public repositories.

---

### 4. Create a `.env` File

In the main project folder, create a file named `.env` (no extension).

Add your API key like this:

```env
OPENWEATHER_API_KEY=your_actual_api_key_here
```

> ❌ Never use someone else’s API key.  
> ❌ Never paste your key in code, chats, or public forums.

---

### 5. Run the App

```bash
python main.py
```

You’ll be prompted to enter a city (e.g., `London`, `Tokyo`, `New York`). Optionally add a country code (e.g., `US`, `JP`, `FR`).

Example:
```
Enter city name (e.g., London): Paris
Enter country code (e.g., GB, US, optional): FR
```

---

## 📁 Project Structure

```
weather-api-project/
├── main.py               # Runs the app
├── weather_api.py        # Core weather logic
├── config.py             # Configuration & API setup
├── .env                  # Your private API key (not shared!)
├── requirements.txt      # Required packages
└── README.md             # This file
```

---

## ⚠️ Security Reminder

- The `.env` file is **ignored in version control** (if you use Git).
- Add `.env` to your `.gitignore`:
  ```bash
  echo ".env" >> .gitignore
  ```
- Always regenerate your API key if accidentally exposed.

---

## 🙌 Credits

Powered by [OpenWeatherMap](https://openweathermap.org/).  
Free for personal and educational use.

---

## 📮 Feedback

Found a bug? Want a feature? Open an issue or contact me!

Happy coding! 🐍🌤️
```

