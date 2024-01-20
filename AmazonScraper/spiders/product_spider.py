import scrapy


class ProductSpiderSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ["amaoizn.com"]
    start_urls = ["https://amaoizn.com"]

    def parse(self, response):
        pass
