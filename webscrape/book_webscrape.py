# webscrape script for
# getting information on books and saving to csv

# info to scrape and save
# title, image, rating, price, availability

# https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/

import requests
import time
import csv
import re
from bs4 import BeautifulSoup as bs


def scrape(url, soup):
    # inspect webpage and books are in article tag, product_pod class
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        # url of book
        # eg: http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
        # h3 -> a -> href
        info_url = url + "/" + book.h3.find("a")["href"]

        title = url + "/" + book.h3.find("a")["title"]

        image_url = url + "/catalogue" + book.a.img["src"].replace("..", "")

        rating = url + "/" + book.find("p", class_="star-rating")["class"][1]

        price = (
            url
            + "/"
            + book.find("p", class_="price_color")
            .text.strip()
            .encode("ascii", "ignore")
            .decode("ascii")
        )

        availability = (
            url + "/" + book.find("p", class_="instock availability").text.strip()
        )

        # function to write into csv with list of items
        write_to_csv([info_url, title, image_url, rating, price, availability])


def write_to_csv(list_input):
    try:
        # open csv as fopen
        with open("Books.csv", "a") as fopen:
            # write into csv
            csv_writer = csv.writer(fopen)

            # iterate keys and values of books and write into csv
            csv_writer.writerow(list_input)
    except:
        return False


# website to scrape
# http://books.toscrape.com/catalogue/page-1.html
# dynamic scraping based on page number
# http://books.toscrape.com/catalogue/page-str({page_number}).html


def browse_scrape(base_url, page_number=1):
    url_pat = re.compile(r"(http://.*\.com)")
    source_url = url_pat.search(base_url).group(0)

    # Page_number from the argument gets formatted in the URL & Fetched
    formatted_url = base_url.format(str(page_number))
    try:
        html_text = requests.get(formatted_url).text

        soup = bs(html_text, "html.parser")
        print(f"Now scraping {formatted_url} ...")

        # when the scrape reaches end of page
        if soup.find("li", class_="next") != None:

            # start scrape script
            scrape(source_url, soup)
            time.sleep(3)

            # increment page number to next page
            page_number += 1

            # function is running recursive till there is no next button
            browse_scrape(base_url, page_number)
        else:
            scrape(source_url, soup)
            return True
        return True

    except Exception as e:
        return e


if __name__ == "__main__":
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    print("Starting web scrape...")

    result = browse_scrape(base_url)

    if result == True:
        print("Web scraping is now complete!")
    else:
        print(f"Oops, That doesn't seem right!!! - {result}")
