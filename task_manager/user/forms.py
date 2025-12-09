from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Enter the username'),
            'class': 'form-control',
        }),
        help_text=_(
            'Required field. Only letters, numbers, and symbols @/./+/-/_.'
        )
    )

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'class': 'form-control'
        }),
        help_text=_('· Your password must contain at least 8 characters.')
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password confirmation'),
            'class': 'form-control'
        }),
        help_text=_('Please enter the password again to confirm.')
    )

    first_name = forms.CharField(
        label=_('First name'),
        widget=forms.TextInput(attrs={
            'placeholder': _('First name'),
            'class': 'form-control'
        })
    )
    last_name = forms.CharField(
        label=_('Last name'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Last name'),
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2'
        ]



class CustomUserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Enter the username'),
            'class': 'form-control',
        }),
        help_text=_(
            'Required field. Only letters, numbers, and symbols @/./+/-/_.'
        )
    )

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'class': 'form-control'
        }),
        help_text=_('· Your password must contain at least 8 characters.')
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password confirmation'),
            'class': 'form-control'
        }),
        help_text=_('Please enter the password again to confirm.')
    )

    first_name = forms.CharField(
        label=_('First name'),
        widget=forms.TextInput(attrs={
            'placeholder': _('First name'),
            'class': 'form-control'
        })
    )
    last_name = forms.CharField(
        label=_('Last name'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Last name'),
            'class': 'form-control'
        })
    )
    class Meta:
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2'
        ]
        model = User

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username).exclude(
            pk=self.instance.pk
        )

        if qs.exists():
            raise forms.ValidationError(_(
                "A user with that username already exists."
            ))
        return username
    