import requests
from ui import *
from utils import *

def show_weather(selected_prof):
    weather_data = None
    city = None
    
    if not selected_prof:
        print("Your don't have a profile! Switching to guest mode...")
        city = input("Enter your city name: ")
    else:
        city = selected_prof["city"]
        
    weather_data = get_weather_data(city)
    if weather_data is None:
        print("Error: weather_data is none!")
        input("Enter to go back: ")
        return 
    
    while True:
        cls()

        weather_menu = "\n=========================WEATHER MENU=========================\n"
        weather_menu += "1. Show all Weather report\n"
        weather_menu += "2. Temperature\n"
        weather_menu += "3. Wind\n"
        weather_menu += "4. Visibility\n"
        weather_menu += "5. Show report of different city\n"
        weather_menu += "6. Exit weather menu\n"

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

        print(weather_menu)
        usr_choice = input('Enter your choice: ')
        cls()

        print()  # Adding Blank space
        if usr_choice == "1":
            print(temperature_data)
            print(wind_data)
            print(visib_data)
            input("Enter to go back: ")
        elif usr_choice == "2":
            print(temperature_data)
            input("Enter to go back: ")
        elif usr_choice == "3":
            print(wind_data)
            input("Enter to go back: ")
        elif usr_choice == "4":
            print(visib_data)
            input("Enter to go back: ")
        elif usr_choice == "5":
            city = input(
                f"""Enter your city name (Your City-{city}): """)
            weather_data = get_weather_data(city)
            if weather_data is None:
                print("Error: weather_data is none!")
                input("Enter to go back: ")
                return
            input("Enter to go back: ")
        elif usr_choice == "6":
            break
        else:
            input("Error: Invalid input (ENTER): ")


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
    
def search_city(city):  # Returns closely matched names
    url = f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data