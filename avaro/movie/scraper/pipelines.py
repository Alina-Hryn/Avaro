# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from avaroapp.models import Movie
from avaroapp.models import Movie, Seance, CinemaMovie, Cinema


class MoviePipeline:
    def process_item(self, item, spider):
        try:
            item['title'] = item['title'].strip().upper()
            movie = Movie.objects.get(title=item['title'])
            # # Already exists, just update it
            instance = item.save(commit=False)
            instance.pk = movie.pk
            instance.save()
        except Movie.DoesNotExist:
            pass

        item.save()
        return item


class CinemaMoviePipeline:
    def process_item(self, item, spider):
        try:
            cinema_movie = CinemaMovie.objects.get(link=item['link'])
            # # Already exists, just update it
            instance = item.save(commit=False)
            instance.pk = cinema_movie.pk
            instance.save()
        except CinemaMovie.DoesNotExist:
            pass

        item.save()
        return item
