import datetime
import uuid
from django.db import models

# Create your models here.

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    igdb_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255,blank=True, default='No name provided')
    summary = models.TextField(default='No description provided')
    release_date = models.DateField(default=datetime.date.today)
    poster_url = models.URLField()

    def __str__(self):
        return self.igdb_id
    

class UserGame(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)

    class Meta:
        unique_together = ["user_id", "game"]

    def __str__(self):
        return self.id