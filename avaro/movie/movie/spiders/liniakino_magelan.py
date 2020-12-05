import scrapy


class LiniakinoMagelanSpider(scrapy.Spider):
    name = 'liniakino_magelan'
    start_urls = ['https://liniakino.com/showtimes/magelan/',
                  'https://liniakino.com/showtimes/metropolis/']

    def parse(self, response):
        # response.css("h1 a").xpath("@href").extract()
        pass
