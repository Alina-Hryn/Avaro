import scrapy


class OskarGulliverSpider(scrapy.Spider):
    name = 'oskar_gulliver'
    allowed_domains = ['https://oskar.kyiv.ua/gulliver/poster']
    start_urls = ['http://https://oskar.kyiv.ua/gulliver/poster/']

    def parse(self, response):
        # response.css("div.main-gallery__name").css("a").xpath("@href").extract()

        pass
