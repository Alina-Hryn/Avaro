import scrapy


class ShevchenkoSpider(scrapy.Spider):
    name = 'shevchenko'
    allowed_domains = ['https://shevchenko.megakino.com.ua/cinema/events']
    start_urls = ['http://https://shevchenko.megakino.com.ua/cinema/events/']

    def parse(self, response):
        pass
