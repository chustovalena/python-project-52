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
        fields = ['name', 'description', 'status', 'executor', 'labels']

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'executor': forms.Select(attrs={'class': 'form-control'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


    