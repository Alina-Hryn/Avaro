import scrapy

from movie.scraper.items import MovieItem, CinemaMovieItem
from avaroapp.models import Movie, CinemaMovie, Cinema


class MultiplexSpider(scrapy.Spider):
    name = 'multiplex'
    # allowed_domains = ['cinemaciti.ua']
    start_urls = ['https://multiplex.ua/ua/movies']

    def parse(self, response):
        items = MovieItem()
        all_urls = response.css(".soon_fm").xpath("@href").extract()
        yield from response.follow_all(all_urls, self.parse_movie)

    def parse_movie(self, response):
        items = MovieItem()
        cinema_movie_items = CinemaMovieItem()
        # cinema_movie_items['link'] = response.url

        items['title'] = response.css("#mvi_title::text").extract_first()
        link = response.css("div.only_video_section").css("h2::attr(data-fullyturl)").extract_first()
        if link is not None:
            link = link.split('?', 1)[0].split('/embed/', 1)
            items['trailer'] = link[0] +'/watch?v=' + link[1]
        items['description'] = response.css('div.movie_description::text').extract_first()
        items['photo'] = 'https://multiplex.ua' + response.css(".poster::attr(src)").extract_first()

        for i in range(1):
            movie = Movie.objects.filter(title=items['title'].strip().upper()).first()
            cinema = Cinema.objects.filter(cinema_network='multiplex').first()
            cinema_movie_items['cinema_id'] = cinema
            cinema_movie_items['movie_id'] = movie
            cinema_movie_items['link'] = response.url
            yield cinema_movie_items

        yield items
