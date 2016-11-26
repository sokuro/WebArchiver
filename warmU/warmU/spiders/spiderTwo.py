import scrapy
from scrapy.selector import HtmlXPathSelector

try:
    from ..items import WarmuItem
except Exception: #ImportError
    from warmU.warmU.items import WarmuItem


class SiteSpider(scrapy.Spider):
    name = "site"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    # need to instantiate a WarmuItem
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//span[@class='pl']")
        items = []
        for titles in titles:
            item = WarmuItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items