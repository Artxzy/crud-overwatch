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

# SÓ POR ENQUANTO

def visaoTanque(request):
    funcoes = Funcao.objects.filter(nome="Tanque")
    herois = Heroi.objects.filter(fk_funcao__nome="Tanque")
    contexto_tanque = {
        "todas_funcoes": funcoes,
        "herois": herois
    }
    return render(request, 'heroistanque.html', contexto_tanque)

def visaoDano(request):
    funcoes = Funcao.objects.filter(nome="Dano")
    herois = Heroi.objects.filter(fk_funcao__nome="Dano")
    contexto_dano = {
        "todas_funcoes": funcoes,
        "herois": herois
    }
    return render(request, 'heroistanque.html', contexto_dano)

def visaoSuporte(request):
    funcoes = Funcao.objects.filter(nome="Suporte")
    herois = Heroi.objects.filter(fk_funcao__nome="Suporte")
    contexto_suporte = {
        "todas_funcoes": funcoes,
        "herois": herois
    }
    return render(request, 'heroistanque.html', contexto_suporte)
