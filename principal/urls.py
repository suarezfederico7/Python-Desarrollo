from django.urls import path
from principal.views import principal, crear_animal, ver_animal

urlpatterns = [
    path('', principal, name='principal'),
    path('crear-animal/', crear_animal, name= 'crear_animal'),
    path('listar-animales/', ver_animal, name='ver_animal')
]