from django import forms
from .models import Semestre

class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = [
            'estudiante',
            'valor',
            'periodo',
        ]

        labels = {
            'estudiante' : 'Estudiante',
            'valor' : 'Valor',
            'periodo' : 'Periodo',
        }