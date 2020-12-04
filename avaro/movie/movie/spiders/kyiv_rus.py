import scrapy


class KyivRusSpider(scrapy.Spider):
    name = 'kyiv_rus'
    allowed_domains = ['https://kievrus.megakino.com.ua/cinema/events']
    start_urls = ['http://https://kievrus.megakino.com.ua/cinema/events/']

    def parse(self, response):
        # response.css(".event-info-list a").css("a").xpath("@href").extract()
        pass
