from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.URLField()
    genres = models.CharField(max_length=255)
    rating = models.CharField(max_length=10)
    year_release = models.IntegerField()
    metacritic_rating = models.IntegerField()
    runtime = models.IntegerField()

    def __str__(self):
        return self.title

