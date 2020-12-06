import scrapy
# from scraper.scraper.items import MovieItem
from ..items import MovieItem
from scrapy.crawler import CrawlerProcess

class LiraSpider(scrapy.Spider):
    name = 'lira'
    allowed_domains = ['lira.megakino.com.ua/']
    start_urls = ['http://lira.megakino.com.ua/cinema/events/']

    def parse(self, response):
        for href in response.css(".event-info-list a").css("a").xpath("@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        # response.css(".event-info-list a").css("a").xpath("@href").extract()

    def parse_dir_contents(self, response):
        print(response.css('.event-background-description'))
        for sel in response.css('.event-background-description'):
            print()
            item = MovieItem()
            item['title'] = sel.css('h1::text').extract_first()
            item['link'] = response.url
            print(item)
            yield item

#
# if __name__ == '__main__':
#     process = CrawlerProcess()
#     process.crawl(LiraSpider)
#     process.start()