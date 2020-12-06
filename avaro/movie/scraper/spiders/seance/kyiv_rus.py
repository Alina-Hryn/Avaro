import scrapy
from avaroapp.models import Movie
# from scraper.scraper.items import MovieItem
from movie.scraper.items import MovieItem
from scrapy.crawler import CrawlerProcess


class KyivRusSpider(scrapy.Spider):
    name = 'kyiv_rus'
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
            item['link'] = response.url
            item['description'] = sel.css('li~ li+ li p::text').extract_first()
            print(item)
            yield item

# if __name__ == '__main__':
#     process = CrawlerProcess()
#     process.crawl(KyivRusSpider)
#     process.start()

# pipeline = MoviePipeline()
# pipeline.process_item()
