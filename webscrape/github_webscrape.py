# webscrape script for
# finding github user profile pic

import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github user: ")
url = "https://github.com/" + github_user
r = requests.get(url)

# prints HTML file
soup = bs(r.content, "html.parser")
# print(soup)

# find img tag with alt: Avatar and retrieve src link
profile_pic = soup.find("img", {"alt": "Avatar"})["src"]
print(profile_pic)
