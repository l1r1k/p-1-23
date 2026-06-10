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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 2px solid pink'}), 
            'description': forms.Textarea(attrs={'class': 'form-control'}), 
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}), 
            'color': forms.TextInput(attrs={'class': 'form-control'}), 
            'size': forms.NumberInput(attrs={'class': 'form-control'}), 
            'category': forms.Select(attrs={'class': 'form-control'}), 
            'collection': forms.SelectMultiple(attrs={'class': 'form-control'}), 
            'is_exists': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }