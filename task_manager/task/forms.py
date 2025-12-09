from .models import Task
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['executor'].queryset = User.objects.all()
        self.fields['executor'].label_from_instance = (
            lambda user: user.get_full_name() or user.username
        )
