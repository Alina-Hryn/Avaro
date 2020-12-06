import scrapy
from avaroapp.models import Movie
# from scraper.scraper.items import MovieItem
from movie.scraper.items import MovieItem


class MegakinoSpider(scrapy.Spider):
    name = 'mega-kino'
    start_urls = ['https://kievrus.megakino.com.ua/cinema/events/',
                  'https://leypzig.megakino.com.ua/cinema/events/',
                  'http://lira.megakino.com.ua/cinema/events/',
                  'https://shevchenko.megakino.com.ua/cinema/events/']

    def parse(self, response):
        for href in response.css(".event-info-list a").css("a").xpath("@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        # response.css(".event-info-list a").css("a").xpath("@href").extract()

    def parse_dir_contents(self, response):
        for sel in response.css('.event-background-description'):
            item = MovieItem()
            item['title'] = sel.css('h1::text').extract_first()
            item['trailer'] = sel.css("a.trailer").xpath("@href").extract_first()
            item['description'] = sel.css('li:nth-child(4) p::text').extract_first()
            item['photo'] = sel.css('.right-event-description img').xpath('@src').extract_first()
            yield item

