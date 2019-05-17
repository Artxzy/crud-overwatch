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


def visaoPorClasse(request, filtro_classe=None):
    funcoes = Funcao.objects.filter(nome__iexact=filtro_classe)
    herois = Heroi.objects.filter(fk_funcao__nome__iexact=filtro_classe)

    contexto_herois = {
        "todas_funcoes": funcoes,
        "herois": herois
    }
    return render(request, 'visao_por_classe.html', contexto_herois)
