import scrapy
from scrapy.linkextractors import LinkExtractor


class ElectronicaSpider(scrapy.Spider):
    name = 'electronica'

    def start_requests(self):
        yield scrapy.Request(
            url="https://exhibitors.electronica.de/exhibitor-portal/2022/list-of-exhibitors/",
            meta={
                "playwright": True,
                "playwright_include_page": True
            },
        )

    def parse(self, response):
        all_exhibitors = response.xpath('//*[@id="jl_contentWrapper"]//*[starts-with(@id, "ceId")]')

        for exhibitor in all_exhibitors:
            company = exhibitor.xpath('.//div[3]/div[1]/h2/a/text()').extract_first()
            url = exhibitor.xpath('.//div[3]/div[1]/h2/a/@href').extract_first()
            if url != None:
                yield { 
                        'Company': company,
                        'Url': url 
                      }
        