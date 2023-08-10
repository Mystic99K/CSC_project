import requests
from pprint import pprint

API_KEY = "5c443b217be241e6b75175940230507"
city = input("Enter city test : ")

def search_city(city):  # Getting API response
    url = f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data


testdata = search_city(city)
pprint(testdata)