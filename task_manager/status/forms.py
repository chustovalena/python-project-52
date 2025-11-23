from .models import Status
from django import forms


class CustomStatusCreationForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'form-control',
            }),
        }
        labels = {
            'name': 'Имя',
        }