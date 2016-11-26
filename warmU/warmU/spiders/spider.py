import hashlib
import os
import htmlmin
import scrapy

from warmU.warmU.items import WarmuItem


class SiteSpider(scrapy.Spider):
    name = "site"
    allowed_domains = ["www.w3schools.com"]
    start_urls = ["http://www.w3schools.com/xml/"]

    def parse(self, response):

        file_name = self.hash_url(response.url)
        directory = 'testdir'

        # if the directory does not exists, build one
        if not os.path.exists(directory):
            os.makedirs(directory)

        # fill the directory with a file of scraped content
        with open(directory + '/' + file_name, 'wb') as f:
            content = htmlmin.minify(response.body.decode('utf-8'))
            f.write(bytes(content, 'utf-8'))


        for anchor in response.xpath('//a'):
            item = WarmuItem()
            item['title'] = anchor.xpath('text()').extract()
            item['link'] = anchor.xpath('@href').extract()
            self.get_children(item)

    def hash_url(self, url):
        return hashlib.md5(url.encode('utf-8')).hexdigest()

    def get_children(self, item):
        print(item)