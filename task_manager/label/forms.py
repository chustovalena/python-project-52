from .models import Label
from django import forms
from django.utils.translation import gettext_lazy as _


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Name'),
            'class': 'form-control'
        })
    )

    class Meta:
        model = Label
        fields = ['name']