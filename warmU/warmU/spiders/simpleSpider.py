# from scrapy.spiders import BaseSpider
import scrapy
from scrapy.selector import HtmlXPathSelector

class SiteSpider(scrapy.Spider):
    name = "site"
    allowed_domains = ['www.w3schools.com']
    start_urls = ["http://www.w3schools.com/xml/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//p")
        for titles in titles:
            title = titles.select("a/text()").extract() # XPath to call the text for the tile
            link = titles.select("@/href").extract()
            print(title, link)
            print (title)