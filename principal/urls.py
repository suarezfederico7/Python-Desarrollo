from django.urls import path
from principal.views import principal, crear_articulo, ver_articulos, ver_detalle, ActualizarArticulo, EliminarArticulo

urlpatterns = [
    path('', principal, name='principal'),
    path('crear-articulo/', crear_articulo, name= 'crear_articulo'),
    path('listar-articulos/', ver_articulos, name='ver_articulos'),
    path('ver-detalle/<articulo_id>/', ver_detalle, name='ver_detalle'),
    path('actualizar-articulo/<pk>/', ActualizarArticulo.as_view(), name='actualizar'),
    path('eliminar-articulo/<pk>/', EliminarArticulo.as_view(), name='eliminar')
]