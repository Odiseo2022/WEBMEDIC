import email
from django import forms

class formulario_consulta(forms.Form):
    
    nombre_completo = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)