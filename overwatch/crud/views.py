from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def visaoInicial(request):
    funcoes = Funcao.objects.all()
    contexto = {
        "todas_funcoes": funcoes
    }
    return render(request, 'index.html', contexto)
