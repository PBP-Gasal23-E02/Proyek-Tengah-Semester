from django.forms import ModelForm
from main.models import Buku
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Buku
        fields = ["Title", "Authors", "Issued", "Language", "Subjects"]

    Title = forms.CharField(widget=forms.TextInput( attrs={'class':'form-control', }), required=False)
    Authors = forms.CharField(widget=forms.TextInput( attrs={'class':'form-control', }), required=False)
    Issued = forms.CharField(widget=forms.TextInput( attrs={'class':'form-control', }), required=False)
    Language = forms.CharField(widget=forms.TextInput( attrs={'class':'form-control', }), required=False)
    Subjects = forms.CharField(widget=forms.TextInput( attrs={'class':'form-control', }), required=False)