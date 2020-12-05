import scrapy
from movie.movie.items import CinemaItem


class CinemaCitiSpider(scrapy.Spider):
    name = 'cinemaciti'
    start_urls = ['https://cinemaciti.ua/about/ocean-plaza']

    def parse(self, response):
        items = CinemaItem()
        items['name'] = response.css(".jumbotron__title::text").extract_first()
        # items['movie_url'] = response.css(".movie__about:nth-child(1) p::text").extract_first()
        # items['address'] = response.css(".cinema-info__item:nth-child(1) .cinema-info__text::text").extract_first()
        # items['address'] = response.css(".info - box__block: nth - child(1).info - box__text").extract_first()
        yield items
