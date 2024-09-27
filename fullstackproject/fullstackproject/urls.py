from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import homeView, cardapioView, formularioView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('home.urls')),
    path('', homeView),
    path('cardapio/', cardapioView, name='cardapioView'),
    path('formulario', formularioView, name='formularioView'),
]

