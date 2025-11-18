from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from principal.models import Articulo
from .forms import PostForm, BuscarArticulo
from django.urls import reverse_lazy

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

    formulario = BuscarArticulo(request.GET)
    if formulario.is_valid():
        tipo_a_buscar = formulario.cleaned_data.get('tipo')
        listado_articulos = Articulo.objects.filter(tipo__icontains=tipo_a_buscar)
    
    return render(request, 'ver_articulos.html', {'lista_de_articulos': listado_articulos, 'formulario': formulario})

def ver_detalle(request, articulo_id):
    articulo = Articulo.objects.get(id=articulo_id)
    return render(request, 'ver_detalle.html', {'articulo': articulo})


class ActualizarArticulo(UpdateView):
    model = Articulo
    template_name = 'actualizar_articulo.html'
    fields = ['marca','color','precio']
    success_url = reverse_lazy('ver_articulos')

class EliminarArticulo(DeleteView):
    model= Articulo
    template_name = 'eliminar_articulo.html'
    success_url = reverse_lazy('ver_articulos')    