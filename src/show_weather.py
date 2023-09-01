import requests
from ui import *
from utils import *
import time

def get_weather_data(city):  # Getting API response
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Could not find weather data for '{city}'.")
        error_handle(response.status_code)
        return None
    
def search_city(city):  # Returns closely matched names
    url = f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        print(f"Could not find city data for '{city}'.")
        error_handle(response.status_code)
        return None

def show_weather(selected_prof):
    weather_data = None
    city = None
    search_data = None
    
    if selected_prof == {}:
        print("Your don't have a profile! Switching to guest mode...")
        city = input("Enter your city name: ")
        search_data = search_city(city)
        unit = unit_menu()
        
    else:
        city = selected_prof["city"]
        search_data = search_city(city)
    
    if len(search_data) > 1:

        print("Did u mean:")
        for i, dict in enumerate(search_data, start=1):
            print(f"{i} . {dict['name']} ({dict['country']})")

        choice = int(input("Enter choice: "))  # Get user input
        city = search_data[choice-1]['name']  # Subtract 1 because list indices start at 0
    
    elif len(search_data) == 1:
        city = search_data[0]['name']
    
    else:
        print('Error: No such city from')
        return

    weather_data = get_weather_data(city)
    if weather_data is None:
        print("Error: weather data is none!")
        input("Enter to go back: ")
        return 
    
    while True:
        cls()
        
        print_menu(
                main_console,
                'Weather Menu',
                'bright_cyan',
                'bright_yellow',
                Text()
                    .append("1. Show Weather report\n")
                    .append("2. Show report of different city\n")
                    .append("3. Exit weather menu")
            )
        
        
        weather_menu = f"Condition: {weather_data['current']['condition']['text']}\n\n"

        weather_menu += f"Temperature: {weather_data['current']['temp_c']}°C\n"
        weather_menu += f"Temperature: {weather_data['current']['temp_f']}°F\n"
        weather_menu += f"Feels like: {weather_data['current']['feelslike_c']}°C\n"
        weather_menu += f"Feels like: {weather_data['current']['feelslike_f']}°F\n\n"
        
        weather_menu += f"Pressure: {weather_data['current']['pressure_mb']}mb\n"
        weather_menu += f"Pressure: {weather_data['current']['pressure_in']}inch\n\n"
        
        weather_menu += f"Precipitation: {weather_data['current']['precip_mm']}mm\n"
        weather_menu += f"Precipitation: {weather_data['current']['precip_in']}inch\n"
        weather_menu += f"Humidity: {weather_data['current']['humidity']}%\n"
        weather_menu += f"Cloud: {weather_data['current']['cloud']}%\n\n"

        weather_menu += f"Wind Speed: {weather_data['current']['wind_mph']}m/h\n"
        weather_menu += f"Max Wind Speed: {weather_data['current']['gust_mph']}m/h\n"
        weather_menu += f"Wind Speed: {weather_data['current']['wind_kph']}km/h\n"
        weather_menu += f"Max Wind Speed: {weather_data['current']['gust_kph']}km/h\n"
        weather_menu += f"Wind Degree: {weather_data['current']['wind_degree']}°\n"
        weather_menu += f"Wind Direction: {weather_data['current']['wind_dir']}\n\n"

        weather_menu += f"Visibility: {weather_data['current']['vis_km']}\n"
        weather_menu += f"Visibility: {weather_data['current']['vis_miles']}\n\n"
        
        weather_menu += f"UV Index: {weather_data['current']['uv']}"
        
        
        weather_pannel = Panel(weather_menu,title='Weather Report',border_style='bright_yellow',style='bright_cyan')

        usr_choice = input('Enter your choice: ')
        cls()

        print()  # Adding Blank space
        if usr_choice == "1":
            main_console.print(weather_pannel)
            input("Enter to go back: ")
            
        elif usr_choice == "2":
            city = input(
                f"""Enter your city name (Your City-{city}): """)
        
            search_data = search_city(city)
        
            if len(search_data) > 1:

                print("Did u mean:")
                for i, dict in enumerate(search_data, start=1):
                    print(f"{i} . {dict['name']} ({dict['country']})")

                choice = int(input("Enter choice: "))  # Get user input
                city = search_data[choice-1]['name']  # Subtract 1 because list indices start at 0
            
            elif len(search_data) == 1:
                city = search_data[0]['name']
            
            else:
                print('Error: No such city from')
                return
            
            print(city)
            
            time.sleep(2)
                
            weather_data = get_weather_data(city)
            
            
            if weather_data is None:
                print("Error: weather_data is none!")
                input("Enter to go back: ")
                return
            
        elif usr_choice == "3":
            break
        else:
            input("Error: Invalid input (ENTER): ")
    