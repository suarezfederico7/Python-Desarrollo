from django.urls import path
from principal.views import principal, crear_articulo, ver_articulos

urlpatterns = [
    path('', principal, name='principal'),
    path('crear-articulo/', crear_articulo, name= 'crear_articulo'),
    path('listar-articulos/', ver_articulos, name='ver_articulos')
]