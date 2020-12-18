import scrapy
from avaroapp.models import *
# from scraper.scraper.items import MovieItem
from movie.scraper.items import *


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
            cinema_movie_items = CinemaMovieItem()
            for i in range(1):
                if 'lira' in response.url:
                    cinema_id = 15
                elif 'kievrus' in response.url:
                    cinema_id = 13
                elif 'shev' in response.url:
                    cinema_id = 16
                else:
                    cinema_id = 14
                movie = Movie.objects.filter(title=item['title'].strip().upper()).first()
                cinema = Cinema.objects.filter(id=cinema_id).first()
                cinema_movie_items['cinema_id'] = cinema
                cinema_movie_items['movie_id'] = movie
                cinema_movie_items['link'] = response.url
                yield cinema_movie_items

            yield item

