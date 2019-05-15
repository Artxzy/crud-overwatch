from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def visaoInicial(request):
    funcoes = Funcao.objects.all()
    herois = Heroi.objects.all()
    contexto = {
        "todas_funcoes": funcoes,
        "herois": herois
    }
    return render(request, 'index.html', contexto)
