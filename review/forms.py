from django.forms import ModelForm
from review.models import *

class ReviewForm(ModelForm):
    class Meta:
        model = ReviewBuku
        fields = ["book", "review_cust"]