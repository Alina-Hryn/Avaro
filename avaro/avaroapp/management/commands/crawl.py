from django.core.management.base import BaseCommand
from movie.movie.spiders.movie.kyiv_rus import KyivRusSpider
from movie.movie.spiders.cinema.cinema_citi import CinemaCitiSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from movie.movie import settings as my_settings



class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        process = CrawlerProcess(crawler_settings)

        # for spider_name in process.spider_loader.list():
        #     print("Running spider %s" % (spider_name))
        #     process.crawl(spider_name, query="dvh")  # query dvh is custom argument used in your scrapy

        process.crawl(CinemaCitiSpider)
        process.start()
