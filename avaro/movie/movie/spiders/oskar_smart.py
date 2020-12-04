import scrapy


class OskarSmartSpider(scrapy.Spider):
    name = 'oskar_smart'
    allowed_domains = ['https://oskar.kyiv.ua/smart/poster']
    start_urls = ['http://https://oskar.kyiv.ua/smart/poster/']

    def parse(self, response):
        # response.css("div.main-gallery__name").css("a").xpath("@href").extract()
        pass
