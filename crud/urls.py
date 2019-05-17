from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', visaoInicial),
    path("tanque/<int:idheroi>/", visaoTanque)
]
