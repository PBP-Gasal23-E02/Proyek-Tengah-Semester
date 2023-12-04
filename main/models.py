from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.IntegerField(null=True, blank=True)
    Type = models.TextField(null=True, blank=True, max_length=255)
    Issued = models.TextField(null=True, blank=True, max_length=255)
    Title = models.TextField(null=True, blank=True, max_length=255)
    Language = models.TextField(null=True, blank=True, max_length=255)
    Authors = models.TextField(null=True, blank=True, max_length=255)
    Subjects = models.TextField(null=True, blank=True, max_length=255)
    LoCC = models.TextField(null=True, blank=True, max_length=255)
    Bookshelves = models.TextField(default="Cookbooks and Cooking", max_length=255)

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)