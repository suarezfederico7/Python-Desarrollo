from django.urls import path
from inicio.views import logueo, registrarse
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',logueo, name='login'),
    path('cerrar-sesion/',LogoutView.as_view(template_name = 'cerrar_sesion.html'), name = 'cerrar_sesion'),
    path('registrarse/', registrarse, name = 'registrarse')
]