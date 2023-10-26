from django.forms import ModelForm
from publication.models import Book

class NewPublicationForm(ModelForm):
    class Meta:
        model = Book
        fields = ["author", "title", "description"]