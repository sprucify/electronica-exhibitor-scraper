import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['electronica.de']
    start_urls = ['https://electronica.de/']

    def parse(self, response):
        pass
