from django.shortcuts import render
from django.conf import settings
from pymongo import MongoClient
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

client = MongoClient('mongodb://localhost:27017/')
db = client['pizzariadatabase']

def homeView(request):
    return render(request, 'index.html')

def cardapioView(request):
    return render(request, 'cardapio.html')

def formularioView(request):
    return render(request, 'formulario.html')

@api_view(['GET', 'POST'])
def cardapio(request):
    if request.method == 'GET':
        pizzas = list(db.pizza.find())
        for pizza in pizzas:
            pizza['_id'] = str(pizza['_id'])
        return Response(pizzas, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        novaPizza = request.data
        insercao = db.pizza.insert_one(novaPizza)
        novaPizza['_id'] = str(insercao.inserted_id)
        return Response(novaPizza, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PUT':
        pass

