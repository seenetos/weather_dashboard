import requests


cities = {
    "hannover": {
        "latitude": 52.3759,
        "longitude": 9.7320
    },
    "berlin": {
        "latitude": 52.52,
        "longitude": 13.405
    }
}


def get_weather_data(city):
    selected_city_latitude = cities[city]["latitude"]
    selected_city_longitude = cities[city]["longitude"]

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={selected_city_latitude}&longitude={selected_city_longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=Europe/Berlin")

    data = response.json()
    current = data["current"]
    current_units = data["current_units"]

    return current, current_units


def display_weather(city, current, current_units):
    print(f"\nCurrent Weather in {city.title()}")
    print("----------------")
    temperature = f"Temperature: {current['temperature_2m']} {current_units['temperature_2m']}"
    humidity = f"Humidity: {current['relative_humidity_2m']} {current_units['relative_humidity_2m']}"
    wind_speed = f"Wind Speed: {current['wind_speed_10m']} {current_units['wind_speed_10m']}"

    print(temperature)
    print(humidity) 
    print(wind_speed)


while True:
    selected_city = input("Please select a city: ").lower()

    if selected_city in cities:
        break

    print("The selected city cannot be found. Please try again.")


current, current_units = get_weather_data(selected_city)
display_weather(selected_city, current, current_units)

