from django.forms import ModelForm
from publication.models import Publication

class NewPublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ["author", "title", "description"]