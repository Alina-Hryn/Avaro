import scrapy

from movie.scraper.items import MovieItem, CinemaMovieItem
from avaroapp.models import Movie, CinemaMovie, Cinema


class MultiplexSpider(scrapy.Spider):
    name = 'multiplex'
    # allowed_domains = ['cinemaciti.ua']
    start_urls = ['https://multiplex.ua/ua/movies']

    def parse(self, response):
        items = MovieItem()
        all_urls = response.css(".soon_fm_name").xpath("@href").extract()
        yield from response.follow_all(all_urls, self.parse_movie)

    def parse_movie(self, response):
        items = MovieItem()
        cinema_movie_items = CinemaMovieItem()
        # cinema_movie_items['link'] = response.url

        items['title'] = response.css("#mvi_title::text").extract_first().strip()
        # items['trailer'] = response.css("a.trailer").xpath("@href").extract_first()
        items['description'] = response.css('div.movie_description p::text').extract_first()
        # items['rating'] = float(response.css('li:nth-child(5) .val::text').extract_first())
        items['country'] = response.css('div.movie_description p::text').extract_first()

        movie = Movie.objects.filter(title=items['title']).all()

        yield items
        # yield {items, cinema_movie_items}
