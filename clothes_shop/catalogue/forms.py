from django import forms
from .models import Category, Collection, Clothe

class ClotheForm(forms.ModelForm):
    class Meta:
        model = Clothe
        fields = [
        'name', 
        'description', 
        'photo',
        'price', 
        'color', 
        'size', 
        'category', 
        'collection', 
        'is_exists'
    ]