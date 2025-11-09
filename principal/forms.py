from django import forms
from .models import Articulo

class PostForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ["tipo", "marca", "color", "precio"]
        labels = {
            "tipo": "(Heladera, Lavarropas, Microondas etc.)",
            "marca": "Escriba la marca del artitulo",
            "color": "Escriba el color del articulo",
            "precio": "Escriba el valor del articulo",
        }
