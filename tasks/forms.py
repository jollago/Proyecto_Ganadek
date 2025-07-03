# forms.py
from django import forms
from .models import Finca

class FincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = ['nombre', 'ubicacion','cedulapropietario','latitud','longitud','hectareas','fuenteagua','explotacion']