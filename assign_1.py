import requests


def get_weather_data(city):
    api_key = "YOUR_GOOGLE_API_KEY"  # Replace with your Google API key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    # Get latitude and longitude of the city
    params = {"address": city, "key": api_key}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        lat, lng = location["lat"], location["lng"]

        # Get weather data using latitude and longitude
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=YOUR_OPENWEATHERMAP_API_KEY"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        return weather_data
    else:
        return None


# Example usage:
city_name = "New York"
weather_info = get_weather_data(city_name)

if weather_info:
    print("Weather Information:")
    print(f"City: {city_name}")
    print(f"Temperature: {weather_info['main']['temp']}°C")
    print(f"Description: {weather_info['weather'][0]['description']}")
else:
    print("Unable to fetch weather data.")


'''
Make sure to replace "YOUR_GOOGLE_API_KEY" and "YOUR_OPENWEATHERMAP_API_KEY" with your actual API keys.
'''