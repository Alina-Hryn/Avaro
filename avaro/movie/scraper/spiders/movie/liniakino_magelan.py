import scrapy
from movie.scraper.items import MovieItem


class LiniakinoMagelanSpider(scrapy.Spider):
    name = 'liniakino_magelan'
    start_urls = [  # 'https://liniakino.com/showtimes/magelan/',
        #               'https://liniakino.com/showtimes/metropolis/',
        'https://liniakino.com/movies/']

    def parse(self, response):
        for href in response.css(".poster").css("a").xpath("@href"):
            print("klwfe")
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        print("qqqq")
        for sel in response.css("#content-inner"):
            item = MovieItem()
            item['title'] = sel.css('h1::text').extract_first()
            item['link'] = sel.css("iframe").xpath("@href").extract_first()
            item['description'] = sel.css('.story::text').extract_first()
            print(item)
            yield item

    # def parse(self, response):
    #     # response.css("h1 a").xpath("@href").extract()
    #     pass
