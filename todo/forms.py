from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """Class to validate forms"""
    class Meta:
        model = Item
        fields = ['name', 'done']
