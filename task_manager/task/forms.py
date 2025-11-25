from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя',
            'class': 'form-control'
        })
    )

    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={
            'placeholder': 'Описание',
            'class': 'form-control',
        })
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']

        widgets = {
            'status': forms.Select(),
            'executor': forms.Select()
        }


    