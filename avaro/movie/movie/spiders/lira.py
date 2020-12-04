import scrapy
from ..items import MovieItem


class LiraSpider(scrapy.Spider):
    name = 'lira'
    allowed_domains = ['lira.megakino.com.ua/']
    start_urls = ['http://lira.megakino.com.ua/cinema/events/']
    next_words = []
    def parse(self, response):
        all_links = response.css(".event-info-list a").css("a").extract()[0]
        next_words = all_links
        yield from response.follow_all(all_links, self.parse_movie)
        print(next_words)

    def parse_movie(self, response):
        items = MovieItem()
        # items['title'] = response.css(".movie__about:nth-child(1) p::text").extract_first()
        # items['movie_url'] = response.css(".movie__about:nth-child(1) p::text").extract_first()
        items['title'] = response.css("h1::text").extract_first()
        yield items
