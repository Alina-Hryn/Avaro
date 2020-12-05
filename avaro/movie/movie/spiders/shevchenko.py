import scrapy


class ShevchenkoSpider(scrapy.Spider):
    name = 'shevchenko'
    start_urls = ['https://shevchenko.megakino.com.ua/cinema/events/']

    def parse(self, response):
        pass
