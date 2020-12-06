from django.core.management.base import BaseCommand
from movie.scraper.spiders.movie.megakino import *
from movie.scraper.spiders.movie.cinema_citi import CinemaCitiSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from movie.scraper import settings as my_settings
from movie.scraper.spiders.movie.multiplex import MultiplexSpider


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        process = CrawlerProcess(crawler_settings)
        movie_list = ["cinemaciti"]
        # print("QWERTY" + str(len(process.spider_loader.list())))
        # for spider_name in process.spider_loader.list():
        #     print("Running spider %s" % (spider_name))
        #     process.crawl("cinemaciti", query="dvh")  # query dvh is custom argument used in your scrapy

        process.crawl(MegakinoSpider)
        process.start()
