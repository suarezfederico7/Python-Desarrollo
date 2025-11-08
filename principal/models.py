from django.db import models

# Create your models here.
class Animal(models.Model):
    especie = models.CharField(max_length=55)
    tipo = models.CharField(max_length=55)
    alimentacion = models.CharField(max_length=55)
    habitat = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.especie.capitalize()}: {self.tipo.capitalize()} - {self.alimentacion.capitalize()} - {self.habitat.capitalize()}"

    

    