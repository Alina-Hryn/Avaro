import scrapy


class OskarSmartSpider(scrapy.Spider):
    name = 'oskar_smart'
    start_urls = ['https://oskar.kyiv.ua/smart/poster/',
                  'https://oskar.kyiv.ua/gulliver/poster/']

    def parse(self, response):
        # response.css("div.main-gallery__name").css("a").xpath("@href").extract()
        pass
