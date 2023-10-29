from django.forms import ModelForm
from bookmark.models import *

class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = ["title","description"]