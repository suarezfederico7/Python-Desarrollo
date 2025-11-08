from django import forms
from .models import Animal

class PostForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["especie", "tipo", "alimentacion", "habitat"]
        labels = {
            "especie": "Especie del Animal (Perro, Gato, etc.)",
            "tipo": "Tipo (Mamifero, Ave, Reptil, Anfibio)",
            "alimentacion": "Alimentación (Hervívoro, Carnívoro, Omnívoro, Carroñero)",
            "habitat": "Hábitat ( Acuático, Terrestre, Aereo, Anfibio)",
        }
