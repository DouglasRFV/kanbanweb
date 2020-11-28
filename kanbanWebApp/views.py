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

def produto_update(request, id):
    print(setor)
    data = {}
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    data['produto'] = produto
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('kanbanWebApp_setor')
    else:
        return render(request, 'kanbanWebApp/update_produto.html', data)     

def painel(request, id):
    #data = {'listaProd': json.dumps(list(produto))}
    
    if request.method == 'POST':
        dataProd = Produto.objects.filter(setor=id)
        produtos = serializers.serialize('json', dataProd)
        #data = {'produtos': produtos}
        #print(data)
        return render(request, 'kanbanWebApp/painel.html', {'produtos': produtos})
