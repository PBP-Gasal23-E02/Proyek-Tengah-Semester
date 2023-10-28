from django.forms import ModelForm
from main.models import Buku

class ProductForm(ModelForm):
    class Meta:
        model = Buku
        fields = ["Title", "Subjects"]