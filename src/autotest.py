import requests
from pprint import pprint
from utils import *

cls()

API_KEY = "5c443b217be241e6b75175940230507"
city = input("Enter city test : ")

def search_city(city):  # Getting API response
    url = f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data


testdata = search_city(city)
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
