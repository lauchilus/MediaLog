import datetime
import uuid
from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    open_library_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    author = models.TextField(blank=True, default='No author provided')
    publish_date = models.DateField(default=datetime.date.today)
    cover_url = models.URLField()

    def __str__(self):
        return self.open_library_id
    

class UserBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    class Meta:
        unique_together = ["user_id", "book"]

    def __str__(self):
        return self.id