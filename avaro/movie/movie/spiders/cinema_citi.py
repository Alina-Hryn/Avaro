import scrapy
from ..items import MovieItem

class CinemaCitiSpider(scrapy.Spider):
    name = 'cinemaciti'
    start_urls = [
        'https://cinemaciti.ua/'
    ]

    def parse(self, response):
        items = MovieItem()
        all_movies = response.css('.poster__info')
        all_urls = response.css(".poster__name").xpath("@href").extract()
        yield from response.follow_all(all_urls, self.parse_movie)
        # for movie in all_movies:
        #     title = movie.css('.poster__name::text').extract_first()
        # title = response.xpath("//a[@class='poster__name']/text()").extract()
        # movie_url = movie.css(".poster__name").xpath("@href").extract_first()
        # movie_url = response.css(".poster__name").xpath("@href").extract()
        # items['title'] = title
        # items['movie_url'] = movie_url
        # items['year'] = year
        #
        # yield items

    def parse_movie(self, response):
        items = MovieItem()
        # items['title'] = response.css(".movie__about:nth-child(1) p::text").extract_first()
        # items['movie_url'] = response.css(".movie__about:nth-child(1) p::text").extract_first()
        items['year'] = response.css(".movie__about:nth-child(1) p::text").extract_first()
        yield items

# if __name__ == '__main__':
#     process = CrawlerProcess()
#     process.crawl(MovieSpider)
#     process.start()


