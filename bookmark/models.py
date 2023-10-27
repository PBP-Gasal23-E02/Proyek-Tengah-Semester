from django.db import models

# Create your models here.
class Buku(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    description = models.TextField()
    bookmarked = models.BooleanField(default=False)