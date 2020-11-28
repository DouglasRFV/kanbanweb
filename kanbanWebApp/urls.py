from django.urls import include, path
from .views import (
    home,
    painel, 
    setor,
    produto_novo,
    produto_update,
)    

urlpatterns = [
    path('', home, name='kanbanWebApp_home'),
    path('painel/<int:id>/', painel, name='kanbanWebApp_painel'),
    path('setor/', setor, name='kanbanWebApp_setor'),
    path('produto-novo/<int:id>', produto_novo, name='kanbanWebApp_produto_novo'),
    path('produto-update/<int:id>/', produto_update, name='kanbanWebApp_produto_update'),
]