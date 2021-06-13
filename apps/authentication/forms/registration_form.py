from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import password_validation
from django import forms

from ..models import User


class RegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ('Los dos campos de contraseña no coinciden.'),
    }
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'autofocus': True, 'placeholder': 'Email'}),
    )

    password1 = forms.CharField(
        label=('Contraseña'),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=('Repetir Contraseña'),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña'}),
    )

    class Meta:
        model = User
        fields = ('email',)
        field_classes = {'email': UsernameField}
