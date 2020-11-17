from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    lote = models.IntegerField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome