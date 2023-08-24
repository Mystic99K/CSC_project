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
                w_console,
                'Weather Menu',
                'bright_cyan',
                'bright_yellow',
                Text()
                    .append("1. Show all Weather report\n")
                    .append("2. Temperature\n")
                    .append("3. Wind\n")
                    .append("4. Visibility\n")
                    .append("5. Show report of different city\n")
                    .append("6. Exit weather menu\n")
            )

        temperature_data = f"Temperature(°C): {weather_data['current']['temp_c']}°C\n"
        temperature_data += f"Temperature(°F): {weather_data['current']['temp_f']}°F\n"
        temperature_data += f"Feels like(°C): {weather_data['current']['feelslike_c']}°C\n"
        temperature_data += f"Feels like(°F): {weather_data['current']['feelslike_f']}°F"

        wind_data = f"Wind Speed(mph): {weather_data['current']['wind_mph']}m/h\n"
        wind_data += f"Max Wind Speed(mph): {weather_data['current']['gust_mph']}m/h\n"
        wind_data += f"Wind Speed(kmph): {weather_data['current']['wind_kph']}km/h\n"
        wind_data += f"Max Wind Speed(kmph): {weather_data['current']['gust_kph']}km/h\n"
        wind_data += f"Wind Degree: {weather_data['current']['wind_degree']}°\n"
        wind_data += f"Wind Direction: {weather_data['current']['wind_dir']}"

        visib_data = f"Visibility(km): {weather_data['current']['vis_km']}\n"
        visib_data += f"Visibility(Miles): {weather_data['current']['vis_miles']}"
        
        temp = Panel(temperature_data,title='Temperature',border_style='bright_yellow',style='bright_cyan')
        wind = Panel(wind_data,title='Wind',border_style='bright_yellow',style='bright_cyan')
        visib = Panel(visib_data,title='Visiblity',border_style='bright_yellow',style='bright_cyan')

        usr_choice = input('Enter your choice: ')
        cls()

        print()  # Adding Blank space
        if usr_choice == "1":
            layout = Layout(name="root")
            layout.split_row(
                Layout(temp),
                Layout(wind),
                Layout(visib),
                )
            m_panel = Panel(layout,title='Weather Data - ' + city ,border_style='bright_yellow',style='bright_cyan')
            w_console.print(m_panel)
            input("Enter to go back: ")
            
        elif usr_choice == "2":
            layout = Layout(name="root")
            layout.split_row(
                Layout(temp),
                )
            m_panel = Panel(layout,title='Weather Data - ' + city,border_style='bright_yellow',style='bright_cyan')
            w_console.print(m_panel)
            input("Enter to go back: ")
            
        elif usr_choice == "3":
            layout = Layout(name="root")
            layout.split_row(
                Layout(wind)
                )
            m_panel = Panel(layout,title='Weather Data',border_style='bright_yellow',style='bright_cyan')
            w_console.print(m_panel)
            input("Enter to go back: ")
            
        elif usr_choice == "4":
            layout = Layout(name="root")
            layout.split_row(
                Layout(visib)
                )
            m_panel = Panel(layout,title='Weather Data')
            w_console.print(m_panel)
            input("Enter to go back: ")
            
        elif usr_choice == "5":
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
            
        elif usr_choice == "6":
            break
        else:
            input("Error: Invalid input (ENTER): ")
    