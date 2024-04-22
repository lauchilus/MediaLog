import uuid
from django.db import models

# Create your models here.

class Serie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tmdb_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_url = models.URLField()

    def __str__(self):
        return self.tmdb_id



class UserSerie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user_id", "serie"]

    def __str__(self):
        return self.id