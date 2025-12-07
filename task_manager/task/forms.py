from .models import Task
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Name'),
            'class': 'form-control'
        })
    )

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs={
            'placeholder': _('Description'),
            'class': 'form-control',
        })
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'executor': forms.Select(attrs={'class': 'form-control'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


    