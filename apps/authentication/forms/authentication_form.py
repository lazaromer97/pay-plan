from django.contrib.auth import forms as auth_forms
from django import forms


class AuthenticationForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'autofocus': True, 'placeholder': 'Email'}),
    )

    password = forms.CharField(
        label=('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
