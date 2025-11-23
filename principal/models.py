from django.db import models

# Create your models here.
class Articulo(models.Model):
    tipo = models.CharField(max_length=55)
    marca = models.CharField(max_length=55)
    color = models.CharField(max_length=55)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen = models.ImageField(upload_to = 'fotos', null = True, blank= True)

    def __str__(self):
        precio_argentino = f"$ {self.precio:,.2f}".replace(",","?").replace(".",",").replace("?",".")
        return f"Tipo: {self.tipo.capitalize()} / Marca: {self.marca.capitalize()} / Color: {self.color.capitalize()} / Valor: {precio_argentino}"

    

    