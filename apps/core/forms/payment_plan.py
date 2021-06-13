from django import forms
from ..models import PaymentPlan


class PaymentPlanForm(forms.ModelForm):
    class Meta:
        model = PaymentPlan
        fields = ['name', 'value', 'recurring']
        labels = {
            'name': 'Name',
            'value': 'Value',
            'recurring': 'Recurring'
        }
        error_messages = {
            'name': {
                'required': ('Por favor ingrese el nombre'),
            },
            'value': {
                'required': ('Por favor ingrese el valor'),
            }
        }
        widgets = {
            'name': forms.TextInput(
                attrs={

                    'id': 'name',
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre',
                    'autocomplete': 'off',
                }
            ),
            'value': forms.NumberInput(
                attrs={
                    'id': 'value',
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor',
                    'min': '0,01',
                    'max': '999999,99',
                }
            ),
            'recurring':  forms.CheckboxInput(
                attrs={
                    'id': 'recurring',
                    'class': 'form-check-input',
                    'type': 'checkbox',
                }
            ),
        }
