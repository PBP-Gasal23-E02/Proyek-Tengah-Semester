from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class WishlistBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    date_added = models.DateField(default=timezone.now)
    