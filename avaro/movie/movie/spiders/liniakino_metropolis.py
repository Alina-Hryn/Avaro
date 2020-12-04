import scrapy


class LiniakinoMetropolisSpider(scrapy.Spider):
    name = 'liniakino_metropolis'
    allowed_domains = ['https://liniakino.com/showtimes/metropolis/']
    start_urls = ['http://https://liniakino.com/showtimes/metropolis//']

    def parse(self, response):
        # response.css("h1 a").xpath("@href").extract()
        pass
