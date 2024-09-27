from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def homeView(request):
    return render(request, 'index.html')

def cardapioView(request):
    return render(request, 'cardapio.html')

def formularioView(request):
    return render(request, 'formulario.html')

@api_view(['GET', 'POST'])
def cardapio(request):
    if request.method == 'GET':
        pizzas = list(settings.db.pizza.find())
        for pizza in pizzas:
            pizza['_id'] = str(pizza['_id'])
            return Response(pizzas)
    elif request.method == 'POST':
        novaPizza = request.data
        settings.db.pizza.insert_one(novaPizza)
        return Response('Pizza adicionada ao cardápio com sucesso!')
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PUT':
        pass

