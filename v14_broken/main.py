import profiles  # Importing profiles.py
import weather_report  # Importing weather_report.py
from clscreen import cls  # Importing clscreen.py

import colors


API_KEY = "5c443b217be241e6b75175940230507"  # trq main acc


while True:

    back = False
    city = profiles.main_menu()  # Getting name of the city

    if city == True:  # Used to end the program

        cls()

        colors.console.print('---Closing Program---', style='error', justify='center')
        break

    while True:
        if city is None:  # Guest user or user wants to enter another city
            city = input(
                "Enter user city name or Enter BACK to go back to profile selection : ")  # Asking user for city

            if city == 'BACK':  # Going back to profiles menu
                break

            weather_data = weather_report.get_weather_data(city, API_KEY)  # Getting weather data from api by providing city
            weather_report.display_weather_data(weather_data)

            cls()

            if back:  # Going back to main menu
                break
            city = None  # Used to ensure no error

        else:  # Profile other than Guest is selected
            weather_data = weather_report.get_weather_data(city, API_KEY)  # Getting weather data from api by providing city
            weather_report.display_weather_data(weather_data)

            cls()

            if back:  # Going back to main menu
                break
            city = None  # User selected to enter another city