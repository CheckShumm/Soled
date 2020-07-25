'''
    Spider dedicated to crawl the following:
    Domain: StockX
    Model: Shoes
    TODO: more thorough description
'''

import scrapy
from bs4 import BeautifulSoup

class SpiderGOAT(scrapy.Spider):
    # for scrappy to identify sraper
    name = 'SpiderGOAT'
    start_urls = ['']
    def __init__(self):   
        self.start_urls = ['http://scraping-challenge-2.herokuapp.com/']
        self.visited = set()

    def parse(self, response):

        soup = BeautifulSoup(response.text, 'html.parser')
        
        yield {
            "CONTENT" : response.text
        }

        #scripts = soup.find_all("script", attrs={"type": "application/ld+json"})


        # if not scripts:
        #     yield {
        #         "ERROR MESSAGE" : response.text
        #     }

        # items_string = scripts[-1].string
        # start = items_string.find('[')
        # items_string = items_string[start::]
        # items_string = items_string.split("}}}")

        # keys = [
        #     "name",
        #     "description",
        #     "lowPrice",
        #     "highPrice",
        #     "url"
        # ]

        # items = list()

        # for item_string in items_string[:-1]:
        #     item = dict()
        #     for key in keys:
        #         data = item_string
        #         data = data[data.find(key)::]
        #         data = data[data.find(':')+1::]
        #         data = data[:data.find(",\"")]
        #         item[key] = data
        #     items.append(item)
        
        # for item in items:
        #     yield {
        #         "name": item["name"], "price": item["lowPrice"], "url": item["url"],
        #     }

        # # store url as visited
        # self.visited.add(response.url)

        # # find all links leading to a sneaker page
        # next_url_list = response.xpath('//a[contains(@href, "/sneakers?page")]/@href').getall()

        # # iterate and visit through all non-visited links
        # for url in next_url_list:
        #     if url in self.visited:
        #         continue

        #     yield scrapy.Request(response.urljoin(url))