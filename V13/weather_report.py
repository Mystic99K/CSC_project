import requests
import colorama
import error


colorama.init()
# Color definitions
################################
c_black = colorama.Fore.BLACK
c_red = colorama.Fore.RED
c_green = colorama.Fore.GREEN
c_yellow = colorama.Fore.YELLOW
c_blue = colorama.Fore.BLUE
c_magenta = colorama.Fore.MAGENTA
c_cyan = colorama.Fore.CYAN
c_white = colorama.Fore.WHITE
c_reset = colorama.Fore.RESET
###############################


def get_weather_data(city,API_KEY):  # Getting API response
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Could not find weather data for {city}.")
        error.error_handle(response.status_code)


def display_weather_data(weather_data):
    while True:
        global back  # Used to go back to profiles menu
        print('1. Show all Weather report')
        print('2. Temperature')
        print('3. Wind')
        print('4. Visibility')
        print('5. Enter a different city')
        print('6. Change profiles')
        choice_w = input('Enter your choice : ')

        if not choice_w.isdigit():  # Checking if input has no alphabets
            print('Error:Invalid Input, Input contained String')
            error.error_handle(100)
            continue
        else:
            choice_w = int(choice_w)

        if choice_w not in [1, 2, 3, 4, 5, 6]:
            print('Error:Invalid Input, Input contained Alphabet or Special character')
            error.error_handle(101)
            continue

        print()  # Adding Blank space
        if choice_w == 1:
            print()
            dis_weather_temp(weather_data)
            print()
            dis_weather_wind(weather_data)
            print()
            dis_weather_vis(weather_data)

        elif choice_w == 2:
            print()
            dis_weather_temp(weather_data)

        elif choice_w == 3:
            print()
            dis_weather_wind(weather_data)

        elif choice_w == 4:
            print()
            dis_weather_vis(weather_data)

        elif choice_w == 5:  # Breaking while loop
            break

        elif choice_w == 6:  # Going back to profiles menu
            back = True
            print()
            break


def dis_weather_temp(weather_data):
    print(c_yellow + 'Temperature' + c_reset)  # Temperature data
    print()
    print(f"Temperature(°C): {weather_data['current']['temp_c']}°C")
    print(f"Temperature(°F): {weather_data['current']['temp_f']}°F")
    print(f"Feels like(°C): {weather_data['current']['feelslike_c']}°C")
    print(f"Feels like(°F): {weather_data['current']['feelslike_f']}°F")


def dis_weather_wind(weather_data):
    print(c_blue + 'Wind' + c_reset)  # Wind data
    print()
    print(f"Wind Speed(mph): {weather_data['current']['wind_mph']}m/h")
    print(f"Max Wind Speed(mph): {weather_data['current']['gust_mph']}m/h")
    print(f"Wind Speed(kmph): {weather_data['current']['wind_kph']}km/h")
    print(f"Max Wind Speed(kmph): {weather_data['current']['gust_kph']}km/h")
    print(f"Wind Degree: {weather_data['current']['wind_degree']}°")
    print(f"Wind Direction: {weather_data['current']['wind_dir']}")


def dis_weather_vis(weather_data):
    print(c_green + 'Visibility' + c_reset)  # Visibility data
    print()
    print(f"Visibility(km): {weather_data['current']['vis_km']}")
    print(f"Visibility(Miles): {weather_data['current']['vis_miles']}")
