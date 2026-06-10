import requests
import json

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.3759&longitude=9.7320&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=Europe/Berlin")
                        
data = response.json()
current = data["current"]
current_units = data["current_units"]

print("Current Weather")
print("----------------")
print(f"Temperature: {current['temperature_2m']} {current_units['temperature_2m']}")
print(f"Humidity: {current['relative_humidity_2m']} {current_units['relative_humidity_2m']}")
print(f"Wind Speed: {current['wind_speed_10m']} {current_units['wind_speed_10m']}")

# Save a sample API response for development and testing
#with open("data/samples/sample_weather.json", "w") as file:
#    json.dump(data, file, indent=4)