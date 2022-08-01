from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cadastro
from .forms import CadastroForm
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')
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

def update_cadastro(request, id):
    cadastro = Cadastro.objects.get(id=id)
    form = CadastroForm(request.POST or None, instance=cadastro)

    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'cadastro.html', {'cadastro': cadastro, 'form': form})

def delete_cadastro(request, id):
    cadastro = Cadastro.objects.get(id=id)

    if request.method == 'POST':
        cadastro.delete()
        return redirect('lista')
    return render(request, 'cadastro.html', {'cadastro': cadastro})