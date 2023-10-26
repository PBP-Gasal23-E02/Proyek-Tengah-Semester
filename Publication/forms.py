from django.forms import ModelForm
from main.models import Book

class NewPublicationForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "main", "description"]