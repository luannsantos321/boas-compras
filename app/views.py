from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cadastro
from .forms import CadastroForm
# Create your views here.

def cadastro(request):
    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(request, 'cadastro.html', {'form': form})

def lista(request):
    lista = Cadastro.objects.all()
    dados = {'lista': lista}
    return render(request, 'lista.html', dados)



