import scrapy


class LiniakinoMagelanSpider(scrapy.Spider):
    name = 'liniakino_magelan'
    allowed_domains = ['https://liniakino.com/showtimes/magelan/']
    start_urls = ['http://https://liniakino.com/showtimes/magelan//']

    def parse(self, response):
        # response.css("h1 a").xpath("@href").extract()
        pass
