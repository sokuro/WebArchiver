import scrapy

# Scrapy schedules the scrapy.Request objects returned by the start_requests method of the Spider. Upon receiving a response for each one, it instantiates <Response> objects and calls the callback method associated with the request(<parse> method) passing the response as argument.

class QuotesSpider(scrapy.Spider):
    # name as unique identification of the spider:
    name = "quotes"

    # return iteration of requests which the Spider will crawl from:
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            # scrapy.Requests objects
            yield scrapy.Request(url=url, callback=self.parse)

    # parse method to handle the response downloaded for each request made:
    # parse() parses the response, extracting the scraped data as dicts and finding new URLs to follow and creating new requests ( Request ) from them.
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)