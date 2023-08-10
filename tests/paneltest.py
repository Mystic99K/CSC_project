from rich import print
from rich.panel import Panel
from rich.columns import Columns
import requests
from pprint import pprint
from /src/utils import *


API_KEY = "5c443b217be241e6b75175940230507"
city = input("Enter city test : ")

def search_city(city):  # Getting API response
    url = f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data


testdata = search_city(city)

print("Did u mean:")
for i, dict in enumerate(testdata, start=1):
    print(f"{i} . {dict['name']} ({dict['country']})")

choice = int(input("Enter choice: "))  # Get user input
mycity = testdata[choice-1]['name']  # Subtract 1 because list indices start at 0

def get_weather_data(city):  # Getting API response
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Could not find weather data for {city}.")
        error_handle(response.status_code)
        return None

weather_data = get_weather_data(mycity)

weather_menu = "\n=========================WEATHER MENU=========================\n"
temperature_data = f"\n=========================TEMPERATURE=========================\n"
temperature_data += f"Temperature(°C): {weather_data['current']['temp_c']}°C\n"
temperature_data += f"Temperature(°F): {weather_data['current']['temp_f']}°F\n"
temperature_data += f"Feels like(°C): {weather_data['current']['feelslike_c']}°C\n"
temperature_data += f"Feels like(°F): {weather_data['current']['feelslike_f']}°F\n"

wind_data = f"\n=========================WIND=========================\n"
wind_data += f"Wind Speed(mph): {weather_data['current']['wind_mph']}m/h\n"
wind_data += f"Max Wind Speed(mph): {weather_data['current']['gust_mph']}m/h\n"
wind_data += f"Wind Speed(kmph): {weather_data['current']['wind_kph']}km/h\n"
wind_data += f"Max Wind Speed(kmph): {weather_data['current']['gust_kph']}km/h\n"
wind_data += f"Wind Degree: {weather_data['current']['wind_degree']}°\n"
wind_data += f"Wind Direction: {weather_data['current']['wind_dir']}\n"

visib_data = f"\n=========================VISIBILITY=========================\n"
visib_data += f"Visibility(km): {weather_data['current']['vis_km']}\n"
visib_data += f"Visibility(Miles): {weather_data['current']['vis_miles']}\n"

# Create three panels
panel1 = Panel("Panel 1 content")
panel2 = Panel("Panel 2 content")
panel3 = Panel("Panel 3 content")

# Put them in a Columns object
columns = Columns([panel1, panel2, panel3])

# Print the columns
print(columns)