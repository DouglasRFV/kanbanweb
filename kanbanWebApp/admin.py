from django.contrib import admin
from .models import (
    Setor,
    Produto
)

admin.site.register(Setor)
admin.site.register(Produto)