import requests
from bs4 import BeautifulSoup as bs
import csv

# get quote and author
# http://quotes.toscrape.com/


def scrape():
    result = requests.get("http://quotes.toscrape.com/")
    page = result.text

    soup = bs(page, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    quote_scraped = []
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("span", class_="author")
        quote_scraped.append([text, author])

        with open("Quotes.csv", "w") as fopen:
            csv_writer = csv.writer(fopen)
            for quote in quote_scraped:
                csv_writer.writerow(quote)
    print(quote_scraped)


# if __name__ == "__main__":
#     print("Starting quote scrape...")
