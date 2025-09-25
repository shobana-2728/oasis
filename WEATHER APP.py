import requests

def get_weather(api_key, city):
    """
    Fetches and displays current weather data for a given city.
    """
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        
        response = requests.get(base_url, params=params)
        
        
        response.raise_for_status() 
        
        
        weather_data = response.json()
        
        
        if weather_data['cod'] == 200:
            main_data = weather_data['main']
            weather_desc = weather_data['weather'][0]['description']
            wind_speed = weather_data['wind']['speed']
            
            temperature = main_data['temp']
            humidity = main_data['humidity']
            
            print(f"--- Weather for {city.title()} ---")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {weather_desc.title()}")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: Could not find weather data for {city}.")
            
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error during API request: {req_err}")
    except KeyError:
        print("Error: Invalid data received from the API.")

if _name_ == "_main_":
    
    your_api_key = "YOUR_API_KEY_HERE"  
    
    
    city_name = input("Enter a city name: ")
    
    
    if your_api_key == "YOUR_API_KEY_HERE":
        print("Please get an API key from OpenWeatherMap and replace 'YOUR_API_KEY_HERE' in the code.")
    else:
        get_weather(your_api_key, city_name)