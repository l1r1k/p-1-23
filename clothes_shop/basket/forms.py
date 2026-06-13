from django import forms

class BasketAddClotheForm(forms.Form):
    count = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Количество',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    reload = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )