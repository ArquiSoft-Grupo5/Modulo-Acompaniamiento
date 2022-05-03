from django import forms
from .models import Acompaniante

class AcompanianteForm(forms.ModelForm):
    class Meta:
        model = Acompaniante
        fields = [
            'name',
            'age',
            'email',
            'sueldo'
        ]
        labels = {
            'name': 'Name',
            'age': 'Age',
            'email': 'Email',
            'sueldo': 'Sueldo',
        }