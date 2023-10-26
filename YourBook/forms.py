from django.forms import ModelForm
from YourBook.models import *

class PinjamBukuForm(ModelForm):
    class Meta:
        model = PinjamBuku
        fields = ["petugas","judul_buku","durasi_pinjam","catatan_peminjaman"]