from django import forms
from django.contrib.auth.forms import AuthenticationForm


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя Пользователя',
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя Пользователя',
            'class': 'form-control'
        })
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        })
    )