from django.shortcuts import redirect, render
from .models import (
    Produto,
    Setor
)

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

def painel(request):
    return render(request, 'kanbanWebApp/painel.html')
