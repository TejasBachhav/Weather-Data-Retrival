import requests

def get_weather(city):
    api_key = "8729098adcbb4cbb865143559231610"  
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data, city):
    if weather_data:
        condition = weather_data["current"]["condition"]["text"]
        temp_c = weather_data["current"]["temp_c"]
        humidity = weather_data["current"]["humidity"]
        wind_kph = weather_data["current"]["wind_kph"]

        print(f"Weather in {city}:")
        print(f"Condition: {condition}")
        print(f"Temperature: {temp_c}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_kph} km/h")
    else:
        print("City not found or API request error.")

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    weather_data = get_weather(city)
    display_weather(weather_data, city)
