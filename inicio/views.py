from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from inicio.forms import FormRegistro

def logueo(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request,usuario)
            return redirect('principal')
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'login.html', {'formulario' : formulario})

def registrarse(request):
    if request.method == "POST":
        formulario = FormRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = FormRegistro()

    return render(request, 'registrarse.html', {'formulario' : formulario})