import requests

# Replace this with your actual API key from https://openweathermap.org/api
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
CITY = "Toronto"  # Change to your preferred city

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = {
            "desc": data["weather"][0]["description"],
            "temp": round(data["main"]["temp"], 1)
        }

        return weather

    except requests.RequestException as e:
        print("Error fetching weather:", e)
        return {"desc": "Unavailable", "temp": "N/A"}


