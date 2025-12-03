from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Имя Пользователя',
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя пользователя',
            'class': 'form-control',
        }),
        help_text='Обязательное поле. Только буквы, цифры и символы @/./+/-/_.'
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }),
        help_text='· Ваш пароль должен содержать как минимум 3 символа.'
    )

    password2 = forms.CharField(
        label='Подтверждение Пароля',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }),
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.'
    )

    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя',
            'class': 'form-control'
        })
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={
            'placeholder': 'Фамилия',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']



class CustomUserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Имя Пользователя',
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя пользователя',
            'class': 'form-control',
        }),
        help_text='Обязательное поле. Только буквы, цифры и символы @/./+/-/_.'
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }),
        help_text='· Ваш пароль должен содержать как минимум 3 символа.'
    )

    password2 = forms.CharField(
        label='Подтверждение Пароля',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }),
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.'
    )

    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя',
            'class': 'form-control'
        })
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={
            'placeholder': 'Фамилия',
            'class': 'form-control'
        })
    )
    class Meta:
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        model = User

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username='username').exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Пользователь с таким username уже существует.")
        return username