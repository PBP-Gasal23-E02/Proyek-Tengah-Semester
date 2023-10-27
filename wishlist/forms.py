from django.forms import ModelForm
from wishlist.models import *

class WishlistBukuForm(ModelForm):
    class Meta:
        model = WishlistBuku
        fields = ["title","description"]