# webscrape script for
# finding github user profile pic
from urllib import response
import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github user: ")
url = "https://github.com/" + github_user
response = requests.get(url)

# prints HTML file
soup = bs(response.content, "html.parser")
# print(soup)

# find img tag with alt: Avatar and retrieve src link
profile_pic = soup.find("img", {"alt": "Avatar"})["src"]
print(profile_pic)
