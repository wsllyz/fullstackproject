from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request, 'index.html')

def cardapioView(request):
    return render(request, 'cardapio.html')

def formularioView(request):
    return render(request, 'formulario.html')