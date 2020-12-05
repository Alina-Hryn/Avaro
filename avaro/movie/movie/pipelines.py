# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from avaroapp.models import Movie
from avaroapp.models import Movie, Cinema


class MoviePipeline:
    def process_item(self, item, spider):
        try:
            movie = Movie.objects.get(title=item['title'])
            # Already exists, just update it
            instance = item.save(commit=False)
            instance.pk = movie.pk
        except Movie.DoesNotExist:
            pass
        item.save()
        return item


class CinemaPipeline:
    def process_item(self, item, spider):
        try:
            movie = Cinema.objects.get(name=item['name'])
            # Already exists, just update it
            instance = item.save(commit=False)
            instance.pk = movie.pk
        except Cinema.DoesNotExist:
            pass
        item.save()
        return item
