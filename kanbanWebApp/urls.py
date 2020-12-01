from django.urls import include, path
from .views import (
    home,
    painel, 
    setor,
    produto_novo,
    produto_update,
    produto_delete,
    perguntas,
)    

urlpatterns = [
    path('', home, name='kanbanWebApp_home'),
    path('perguntas-frequentes', perguntas, name='kanbanWebApp_perguntas'),
    path('painel/<int:id>/', painel, name='kanbanWebApp_painel'),
    path('setor/', setor, name='kanbanWebApp_setor'),
    path('produto-novo/<int:id>', produto_novo, name='kanbanWebApp_produto_novo'),
    path('produto-update/<slug:param1>/<slug:param2>', produto_update, name='kanbanWebApp_produto_update'),
    path('produto-delete/<slug:param1>/<slug:param2>', produto_delete, name='kanbanWebApp_produto_delete'),
]