from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from principal.models import Animal
from .forms import PostForm

# Create your views here.

def principal(request):
    # return HttpResponse('<h1>Proyecto Principal</h1>')
    return render(request, 'principal.html')

def crear_animal(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Animal guardado correctamente.")
            form = PostForm()  
        else:
            form.add_error(None, "Error en el grabado")        
    else:
        form = PostForm()     

    return render(request, 'crear_animal.html', context={"form":form})

def ver_animal(request):

    animales = Animal.objects.all()
    
    return render(request, 'ver_animales.html', {'lista_de_animales': animales})