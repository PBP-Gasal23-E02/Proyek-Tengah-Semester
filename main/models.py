from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.IntegerField(null=True, blank=True)
    Type = models.CharField(null=True, blank=True, max_length=255)
    Issued = models.CharField(null=True, blank=True, max_length=255)
    Title = models.CharField(null=True, blank=True, max_length=255)
    Language = models.CharField(null=True, blank=True, max_length=255)
    Authors = models.CharField(null=True, blank=True, max_length=255)
    Subjects = models.CharField(null=True, blank=True, max_length=255)
    LoCC = models.CharField(null=True, blank=True, max_length=255)
    Bookshelves = models.CharField(null=True, blank=True, max_length=255)

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)