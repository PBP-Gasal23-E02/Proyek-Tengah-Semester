from django.forms import ModelForm, HiddenInput
from publication.models import Publication
from django import forms

class NewPublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ["author", "title", "subjects", "language", "bookshelves", "locc"]
        widgets = {
            "author": forms.TextInput(attrs={"required": True}),
            "title": forms.TextInput(attrs={"required": True}),
            "issued": HiddenInput(),
        }