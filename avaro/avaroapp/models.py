from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title
