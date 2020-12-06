import scrapy


class KinoboomerSpider(scrapy.Spider):
    name = 'kinoboomer'
    allowed_domains = ['https://kinoboomer.com.ua/']
    start_urls = ['http://https://kinoboomer.com.ua//']

    def parse(self, response):
        all_links = response.css("h2 a").xpath("@href").extract()
