# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from avaroapp.models import Movie
from avaroapp.models import Movie



class MoviePipeline:
    def process_item(self, item, spider):
        # movie = Movie()
        # movie.title = item['title']
        # movie.link = item['link']
        # movie.save()
        print("Pipeline " + item['link'])
        item.save()
        return item

