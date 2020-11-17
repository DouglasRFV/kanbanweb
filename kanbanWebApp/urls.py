from django.urls import include, path
from .views import (
    home,
    painel, 
    setor,
)    

urlpatterns = [
    path('', home, name='kanbanWebApp_home'),
    path('painel/', painel, name='kanbanWebApp_painel'),
    path('setor/', setor, name='kanbanWebApp_setor'),
]