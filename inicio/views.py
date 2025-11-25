from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from inicio.forms import FormRegistro, FormModificacion, AvatarForm
from django.contrib.auth.decorators import login_required
from inicio.models import Avatar


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

def perfil(request):
    return render(request, 'perfil.html')

@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = FormModificacion(request.POST, instance=request.user)
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None

        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance  = avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)

        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect('perfil')
    else:
        form = FormModificacion(instance=request.user)
        if hasattr(request.user, "avatar"):
            avatar_form = AvatarForm(instance = request.user.avatar)
        else:
            avatar_form = AvatarForm()    
    return render(request, 'editar_perfil.html', {'form': form, 'avatar_form' : avatar_form})

