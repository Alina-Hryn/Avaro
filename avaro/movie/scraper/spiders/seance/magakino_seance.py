from datetime import datetime

import scrapy
from avaroapp.models import Movie, Cinema, CinemaMovie
# from scraper.scraper.items import MovieItem
from movie.scraper.items import MovieItem, SeanceItem, CinemaMovieItem
from scrapy.crawler import CrawlerProcess


class MegakinoSeance(scrapy.Spider):
    name = 'megakino_seance'
    start_urls = ['https://w.megakino.com.ua/agent14sitekievrus/widget/site',
                  'https://w.megakino.com.ua/agent10siteleypzig/widget/site',
                  'https://w.megakino.com.ua/agent5sitelira/widget/site',
                  'https://w.megakino.com.ua/agent11siteshev/widget/site']

    def parse(self, response):
        for href in response.css(".event-timetable"):
            cinema_movie = CinemaMovie()
            movie_item = MovieItem()
            item = SeanceItem()
            date = href.css(".timetable-date::text").extract_first().strip().split(' ', 1)[0]
            # item['date'] = datetime(year=2020, month=datetime.now().month, day=int(date))
            for sel in href.css(".row-timetable::text"):
                movie_item['title'] = href.css(".name-timetable::text").extract_first().strip().upper()
                print(movie_item['title'])
                if 'lira' in response.url:
                    cinema_id = 15
                elif 'kievrus' in response.url:
                    cinema_id = 13
                elif 'shev' in response.url:
                    cinema_id = 16
                else:
                    cinema_id = 14
                movie = Movie.objects.filter(title=movie_item['title']).first()
                cinema = Cinema.objects.filter(id=cinema_id).first()
                cinema_movie = CinemaMovie.objects.filter(cinema_id=cinema, movie_id=movie).first()
                item['cinema_movie_id'] = cinema_movie
                item['link'] = href.css(".button-common::attr(href)").extract_first()
                # item['description'] = sel.css('li~ li+ li p::text').extract_first()
                print(item)
                yield item


