from django.shortcuts import redirect, render
from .models import (
    Produto,
    Setor
)
import json
from django.core import serializers

def home(request):
    return render(request, 'kanbanWebApp/index.html')

def setor(request):
    if request.method == 'POST':
        idSetor = request.POST['selectSetor']
        produtos = Produto.objects.filter(setor=idSetor)
        data = {'produtos': produtos, 'idSetor': idSetor}
        return render(request, 'kanbanWebApp/setor.html', data)
    else:
        produtos = Produto.objects.all()
        data = {'produtos': produtos}
        return render(request, 'kanbanWebApp/setor.html', data)

def painel(request, id):
    #data = {'listaProd': json.dumps(list(produto))}
    
    if request.method == 'POST':
        dataProd = Produto.objects.filter(setor=id)
        produtos = serializers.serialize('json', dataProd)
        #data = {'produtos': produtos}
        #print(data)
        return render(request, 'kanbanWebApp/painel.html', {'produtos': produtos})
