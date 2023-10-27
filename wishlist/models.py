from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class WishlistBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_added = models.DateField(default=timezone.now)
    # review buku nanti