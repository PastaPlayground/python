from email.quoprimime import body_check
from fileinput import filename
from subprocess import call
import scrapy

# scrapy bot for quotes
class QuotesSpider(scrapy.Spider):
    # define name for spider
    name = "Quotes"

    def start_requests(self):
        # url to scrape
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"

        # write file, open in binary mode
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
