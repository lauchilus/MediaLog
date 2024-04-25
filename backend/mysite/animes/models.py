import datetime
import uuid
from django.db import models

# Create your models here.

class Anime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mal_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255,blank=True, default='No name provided')
    synopsis = models.TextField(blank=True, default='No description provided')
    release_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    poster_url = models.URLField()

    def __str__(self):
        return self.mal_id
    

class UserAnime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    class Meta:
        unique_together = ["user_id", "anime"]

    def __str__(self):
        return self.id