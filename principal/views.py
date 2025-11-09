from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from principal.models import Articulo
from .forms import PostForm

# Create your views here.

def principal(request):
    # return HttpResponse('<h1>Proyecto Principal</h1>')
    return render(request, 'principal.html')

def crear_articulo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Articulo guardado correctamente.")
            form = PostForm()  
        else:
            form.add_error(None, "Error en el grabado")        
    else:
        form = PostForm()     

    return render(request, 'crear_articulo.html', context={"form":form})

def ver_articulos(request):

    articulos = Articulo.objects.all()
    
    return render(request, 'ver_articulos.html', {'lista_de_articulos': articulos})