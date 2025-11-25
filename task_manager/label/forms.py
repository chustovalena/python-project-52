from .models import Label
from django import forms


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Label
        fields = ['name']