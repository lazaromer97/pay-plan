from django.contrib.auth import forms as auth_forms
from django.contrib.auth import password_validation
from django import forms


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    error_messages = {
        'password_mismatch': ('Los dos campos de contraseña no coinciden.'),
        'password_incorrect': ('Su antigua contraseña es incorrecta. Por favor, vuelva a introducirla.'),
    }

    old_password = forms.CharField(
        label=('Vieja Contraseña'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autofocus': True, 'placeholder': 'Vieja Contraseña'}),
    )

    new_password1 = forms.CharField(
        label=('Nueva Contraseña'),
        widget=forms.PasswordInput(attrs={'placeholder': 'Nueva Contraseña'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label=('Confirmar Nueva Contraseña'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmar Nueva Contraseña'}),
    )
