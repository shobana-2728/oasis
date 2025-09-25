import requests

API_KEY = "99ca9c5ce0ae0b10e5ea21653ca54d21"   
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        data = resp.json()
        if resp.status_code != 200:
            print("❌ City not found or API error. Message:", data.get("message"))
            return
        name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        print(f"\nWeather in {name}:")
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {desc.capitalize()}")
    except requests.exceptions.Timeout:
        print("⚠ Request timed out. Check your internet.")
    except requests.exceptions.RequestException as e:
        print("⚠ Network error:", e)

if __name__ == "__main__":
    city = input("Enter city name (e.g., Chennai): ").strip()
    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")
