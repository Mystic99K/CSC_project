import requests
import colorama
import profiles  # Importing profiles.py
import error  # Importing error.py

colorama.init()
# Color definitons
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


API_KEY = "5c443b217be241e6b75175940230507"  # trq main acc


def get_weather_data(city):  # Getting API response
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Could not find weather data for {usr_city}.")
        error.error_handle(response.status_code)


def dis_weather_temp():
    print(c_yellow + 'Temperature' + c_reset)  # Temperature data
    print()
    print(f"Temperature(°C): {weather_data['current']['temp_c']}°C")
    print(f"Temperature(°F): {weather_data['current']['temp_f']}°F")
    print(f"Feels like(°C): {weather_data['current']['feelslike_c']}°C")
    print(f"Feels like(°F): {weather_data['current']['feelslike_f']}°F")
    print()
    print()


def dis_weather_wind():
    print(c_blue + 'Wind' + c_reset)  # Wind data
    print()
    print(f"Wind Speed(mph): {weather_data['current']['wind_mph']}m/h")
    print(f"Max Wind Speed(mph): {weather_data['current']['gust_mph']}m/h")
    print(f"Wind Speed(kmph): {weather_data['current']['wind_kph']}km/h")
    print(f"Max Wind Speed(kmph): {weather_data['current']['gust_kph']}km/h")
    print(f"Wind Degree: {weather_data['current']['wind_degree']}°")
    print(f"Wind Direction: {weather_data['current']['wind_dir']}")
    print()
    print()


def dis_weather_vis():
    print(c_green + 'Visibility' + c_reset)  # Visibility data
    print()
    print(f"Visibility(km): {weather_data['current']['vis_km']}")
    print(f"Visibility(Miles): {weather_data['current']['vis_miles']}")
    print()
    print()


def calling():
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
            print('Error:Invalid Input,Input contained String')
            error.error_handle(100)
            continue
        else:
            choice_w = int(choice_w)

        print()  # Adding Blank space
        if choice_w == 1:
            dis_weather_temp()
            dis_weather_wind()
            dis_weather_vis()
        elif choice_w == 2:
            dis_weather_temp()
        elif choice_w == 3:
            dis_weather_wind()
        elif choice_w == 4:
            dis_weather_vis()
        elif choice_w == 5:  # Breaking while loop
            break
        elif choice_w == 6:  # Going back to profiles menu
            back = True
            break
        else:
            print('Error:Invalid input')
            error.error_handle(101)


while True:
    back = False
    usr_city = profiles.main_menu()
    if usr_city == True:  # Used to end the program
        print('Closing Program...')
        break
    while True:
        if usr_city == 'Null':  # Guest user or user wants to enter another city
            usr_city = input(
                "Enter user city name or Enter BACK to go back to profile selection : ")  # Asking user for city
            if usr_city == 'BACK':  # Going back to profiles menu
                break
            weather_data = get_weather_data(usr_city)  # Getting weather data from api by providing city
            calling()
            if back:
                break
            usr_city = 'Null'  # Used to ensure no error
        else:  # Profile other than Guest is selected
            weather_data = get_weather_data(usr_city)  # Getting weather data from api by providing city
            calling()
            if back:
                break
            usr_city = 'Null'  # User selected to enter another city
