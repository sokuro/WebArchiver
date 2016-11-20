# from scrapy.spider import BaseSpider
import scrapy
from scrapy.selector import HtmlXPathSelector
from warmU.warmU.items import WarmuItem


class SiteSpider(scrapy.Spider):
    name = "site"
    allowed_domains = ['www.w3schools.com']
    start_urls = ["http://www.w3schools.com/xml/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//p")
        items = []
        for titles in titles:
            item = WarmuItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").exctract()
            items.append(item)
        return items