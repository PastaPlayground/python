# Weather App using API calls from openweather
# GET response in JSON format
# turn json into proper format
# display results

import requests
import config

# import API_KEY from config
city = input("Enter a city: ")

# url to get results
api_url = (
    "https://api.openweathermap.org/data/2.5/weather?appid="
    + config.API_Key
    + "&q="
    + city
    + "&units=metric"
)

# .json()
# convert to json format
weather_data = requests.get(api_url).json()

country_name = weather_data["name"]

# temp
temp = weather_data["main"]["temp"]

# extract data from json
print(f"The current temperature for {country_name} is {temp} degree celsius.")
