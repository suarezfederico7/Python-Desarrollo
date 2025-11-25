from django import forms
from .models import Articulo

class PostForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ["tipo", "marca", "color", "precio","imagen"]
        labels = {
            "tipo": "Tipo: (Heladera, Lavarropas, Microondas etc.)",
            "marca": "Escriba la marca del artitulo",
            "color": "Escriba el color del articulo",
            "precio": "Escriba el valor del articulo",
            "imagen": "Subir imagen",
        }

class BuscarArticulo(forms.Form):
    tipo = forms.CharField(max_length=55, required=False)

