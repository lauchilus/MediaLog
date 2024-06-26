import datetime
import uuid
from django.db import models

# Create your models here.

class Serie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tmdb_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255, default='No name provided')
    overview = models.TextField(blank=True, default='No description provided')
    release_date = models.DateField(default=datetime.date.today)
    poster_url = models.URLField()

    def __str__(self):
        return self.tmdb_id



class UserSerie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)

    class Meta:
        unique_together = ["user_id", "serie"]

    def __str__(self):
        return self.id