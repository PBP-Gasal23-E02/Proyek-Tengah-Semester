from django.db import models
from main.models import Buku
from django.contrib.auth.models import User

# Create your models here.

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField()
