# Weather App using API calls
# GET response in JSON format
# turn json into proper format
# display results

import requests

API_Key = "0a56b803a8352ea281ff94090bc7c94a"
city = input("Enter a city: ")

# url to get results
api_url = (
    "https://api.openweathermap.org/data/2.5/weather?appid="
    + API_Key
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
