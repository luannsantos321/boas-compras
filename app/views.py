from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cadastro
# Create your views here.

def cadastro(request):
    return render(request, 'cadastro.html')

def lista(request):
    lista = Cadastro.objects.all()
    dados = {'lista': lista}
    return render(request, 'lista.html', dados)

