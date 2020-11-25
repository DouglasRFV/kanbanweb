from django.urls import include, path
from .views import (
    home,
    painel, 
    setor,
    updatePainel
)    

urlpatterns = [
    path('', home, name='kanbanWebApp_home'),
    path('painel/<int:id>/', painel, name='kanbanWebApp_painel'),
    path('painel-update/<int:id>/', updatePainel, name='kanbanWebApp_updatePainel'),
    path('setor/', setor, name='kanbanWebApp_setor'),
]