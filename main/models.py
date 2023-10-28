from django.db import models

class Buku(models.Model):
    Text = models.IntegerField(null=True, blank=True)
    Type = models.TextField(null=True, blank=True)
    Issued = models.TextField(null=True, blank=True)
    Title = models.TextField(null=True, blank=True)
    Language = models.TextField(null=True, blank=True)
    Authors = models.TextField(null=True, blank=True)
    Subjects = models.TextField(null=True, blank=True)
    LoCC = models.TextField(null=True, blank=True)
    Bookshelves = models.TextField(null=True, blank=True)

