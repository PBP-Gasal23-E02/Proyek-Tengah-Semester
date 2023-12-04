from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.TextField(null=True, blank=True)
    Type = models.TextField(null=True, blank=True)
    Issued = models.TextField(null=True, blank=True)
    Title = models.TextField(null=True, blank=True)
    Language = models.TextField(null=True, blank=True)
    Authors = models.TextField(null=True, blank=True)
    Subjects = models.TextField(null=True, blank=True)
    LoCC = models.TextField(null=True, blank=True)
    Bookshelves = models.TextField(default="Cookbooks and Cooking")

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)