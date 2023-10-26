from django.db import models

class Buku(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    description = models.TextField()
