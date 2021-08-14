#Final_Project_FloresMarroqin
#CIS 245
#Weather App


from requests.api import get


def getWeatherCity(cz):
    import requests
    import json

    ow_url1 = "http://api.openweathermap.org/data/2.5/weather?"
    api_key1 = "&appid=e762dedd5a8fac0c00d6dc1243031872"
    city = "q=" + cz
    full_url1 = ow_url1 + city + api_key1 + "&units=imperial"
    response1 = requests.get(full_url1).json()
    print(response1)

def getWeatherZip(cz):
    import requests
    import json

    ow_url2 = "http://api.openweathermap.org/data/2.5/weather?"
    api_key2 = "&appid=e762dedd5a8fac0c00d6dc1243031872"
    zip = "&zip=" + cz
    full_url2 = ow_url2 + api_key2 + zip + "&units=imperial"
    response2 = requests.get(full_url2).json()
    print(response2)
    

print("Welcome to Instant Weather! Let's see how it feels in YOUR town!")
cz = input("Please enter your city name or Zip code: ")

if cz.isdigit():
    getWeatherZip(cz)
else:
    getWeatherCity(cz)
