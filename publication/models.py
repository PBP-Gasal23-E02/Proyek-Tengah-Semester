from django.db import models
from main.models import Buku
from django.contrib.auth.models import User

# Create your models here.

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    issued = models.DateField(auto_now_add=True)
    subjects = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    bookshelves = models.CharField(default="Cookbooks and Cooking", max_length=255)
    locc = models.CharField(default="TX", max_length=255)