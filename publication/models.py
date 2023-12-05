from django.db import models
from main.models import Buku
from django.contrib.auth.models import User

# Create your models here.

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    author = models.TextField(null=True)
    title = models.TextField(null=True)
    issued = models.DateField(auto_now_add=True, null=True)
    subjects = models.TextField(null=True)
    language = models.TextField(null=True)
    bookshelves = models.TextField(default="Cookbooks and Cooking")
    locc = models.TextField(default="TX")