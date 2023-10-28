from django.db import models
from django.contrib.auth.models import User
from main.models import Buku
# Create your models here.
class PinjamBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    petugas = models.CharField(max_length=255)
    judul_buku = models.CharField(max_length=255)
    durasi_pinjam = models.IntegerField()
    catatan_peminjaman = models.TextField()