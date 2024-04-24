import datetime
import uuid
from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tmdb_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255,blank=True, default='No name provided')
    overview = models.TextField(blank=True, default='No description provided')
    release_date = models.DateField()
    poster_url = models.URLField()

    def __str__(self):
        return self.tmdb_id


class UserMovies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)

    class Meta:
        unique_together = ["user_id", "movie"]

    def __str__(self):
        return self.id

