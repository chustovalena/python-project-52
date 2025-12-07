from .models import Status
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomStatusCreationForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Name'),
                'class': 'form-control',
            }),
        }
        labels = {
            'name': _('Name'),
        }