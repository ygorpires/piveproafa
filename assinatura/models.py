from django.db import models
from producao.models import Produto
from django.conf import settings


class Pacote(models.Model):
    nome=models.CharField(max_length=100)
    produtos= models.ManyToManyField(Produto,blank=False)

class TipoPagamento(models.Model):
    tipo = models.CharField(max_length=45)

class Assinatura(models.Model):
    preco = models.DecimalField(max_digits=3,decimal_places=2)
    sazonalidade = models.CharField(max_length=45)
    data_pagamento = models.DateField(auto_now=False, auto_now_add=False)
    tipo_pagamento= models.OneToOneField(TipoPagamento,null=False,blank=False,on_delete= models.PROTECT)
    pacotes= models.ManyToManyField(Pacote, blank=False)





