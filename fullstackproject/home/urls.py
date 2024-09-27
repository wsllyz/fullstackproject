from django.urls import path
from home.views import cardapio

urlpatterns = [
    path('', cardapio,),
]
