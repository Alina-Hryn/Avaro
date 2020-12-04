import scrapy


class LeypzigSpider(scrapy.Spider):
    name = 'leypzig'
    allowed_domains = ['https://leypzig.megakino.com.ua/cinema/events']
    start_urls = ['http://https://leypzig.megakino.com.ua/cinema/events/']

    def parse(self, response):
        # response.css(".event-info-list a").css("a").xpath("@href").extract()
        pass
