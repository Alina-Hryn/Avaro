import scrapy
from movie.scraper.items import MovieItem


class CinemaCitiSpider(scrapy.Spider):
    name = 'cinemaciti_movie'
    start_urls = [
        'https://cinemaciti.ua/'
    ]

    def parse(self, response):
        items = MovieItem()
        all_movies = response.css('.poster__info')
        all_urls = response.css(".poster__name").xpath("@href").extract()
        yield from response.follow_all(all_urls, self.parse_movie)

    def parse_movie(self, response):
        items = MovieItem()
        items['title'] = response.css(".movie-video-container__name-ukr::text").extract_first().strip()
        items['year'] = response.css(".movie__about:nth-child(1) p::text").extract_first()
        items['trailer'] = response.css("a.trailer").xpath("@href").extract_first()
        items['description'] = response.css('.movie__description p::text').extract_first().strip()
        items['photo'] = 'https://cinemaciti.ua/' + response.css('.movie__img img').xpath('@src').extract_first()
        yield items

# if __name__ == '__main__':
#     process = CrawlerProcess()
#     process.crawl(MovieSpider)
#     process.start()
