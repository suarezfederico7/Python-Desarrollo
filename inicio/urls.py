from django.urls import path
from inicio.views import logueo, registrarse, perfil, editar_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',logueo, name='login'),
    path('cerrar-sesion/',LogoutView.as_view(template_name = 'cerrar_sesion.html'), name = 'cerrar_sesion'),
    path('registrarse/', registrarse, name = 'registrarse'),
    path('perfil/', perfil, name = 'perfil'),
    path('editar-perfil/', editar_perfil, name = 'editar_perfil')
]