import requests
from bs4 import BeautifulSoup as bs

for i in range(50):
    r = requests.get("https://www.name-generator.org.uk/quick/")
    page = r.text
    soup = bs(page, "html.parser")

    names = soup.find_all("div", class_="name_heading")

    file = open("usernames.txt", 'a')
    for name in names:
        print(name.contents[0])
        file.write(f'{name.contents[0]}\n')
