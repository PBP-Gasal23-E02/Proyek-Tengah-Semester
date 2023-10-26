from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField()