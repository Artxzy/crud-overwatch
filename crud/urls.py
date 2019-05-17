from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "herois"

urlpatterns = [
    path('', visaoInicial,name="pagina_inicial"),
    path("classe/<str:filtro_classe>/", visaoPorClasse, name="visao_por_classe")
]
