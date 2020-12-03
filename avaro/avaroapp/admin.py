from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Movie, MovieAdmin)

