from django.db import models
# from YourBook.models import Products
# Create your models here.

class Book(models.Model):
    # book = models.ForeignKey(Products, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField()

