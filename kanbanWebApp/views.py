from django.shortcuts import redirect, render
from .models import (
    Produto,
    Setor
)
import json
from django.core import serializers
from .forms import ProdutoForm

def home(request):
    return render(request, 'kanbanWebApp/index.html')

def perguntas(request):
    return render(request, 'kanbanWebApp/perguntas_frequentes.html')

def setor(request):
    if request.method == 'POST':
        idSetor = request.POST['selectSetor']
        produtos = Produto.objects.filter(setor=idSetor)
        form = ProdutoForm()
        data = {'produtos': produtos, 'idSetor': idSetor, 'form': form}
        return render(request, 'kanbanWebApp/setor.html', data)
    else:
        produtos = Produto.objects.all()
        data = {'produtos': produtos}
        return render(request, 'kanbanWebApp/setor.html', data)

def produto_novo(request, id):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
    idSetor = id
    produtos = Produto.objects.filter(setor=idSetor)
    form = ProdutoForm()
    data = {'produtos': produtos, 'idSetor': idSetor, 'form': form}
    return render(request, 'kanbanWebApp/setor.html', data)

def produto_update(request, param1, param2):

    data = {}
    produto = Produto.objects.get(id=param1)
    form = ProdutoForm(request.POST or None, instance=produto)
    data['produto'] = produto
    data['form'] = form
    data['idSetor'] = param2

    if request.method == 'POST':
        if form.is_valid():
            idSetor = param2
            produtos = Produto.objects.filter(setor=idSetor)
            form.save()
            form = ProdutoForm()
            data = { 'produtos': produtos, 'idSetor': idSetor, 'form': form }
            return render(request, 'kanbanWebApp/setor.html', data)
    else:
        data = {}
        produto = Produto.objects.get(id=param1)
        form = ProdutoForm(request.POST or None, instance=produto)
        data['produto'] = produto
        data['form'] = form
        data['idSetor'] = param2
        return render(request, 'kanbanWebApp/update_produto.html', data)

def produto_delete(request, param1, param2):
    if request.method == 'POST':
        produto = Produto.objects.get(id=param1)
        produto.delete()
        idSetor = param2
        produtos = Produto.objects.filter(setor=idSetor)
        form = ProdutoForm()
        data = { 'produtos': produtos, 'idSetor': idSetor, 'form': form }
        return render(request, 'kanbanWebApp/setor.html', data)
    else:
        produto = Produto.objects.get(id=param1)
        return render(request, 'kanbanWebApp/delete_confirm.html', { 'objDelete': produto })

def painel(request, id):
    if request.method == 'POST':
        dataProd = Produto.objects.filter(setor=id)
        produtos = serializers.serialize('json', dataProd)
        return render(request, 'kanbanWebApp/painel.html', {'produtos': produtos})
