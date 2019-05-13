from django.db import models
from cliente.models import Cliente


class Endereco(models.Model):
    logradouro = models.CharField(max_length=80,null=True)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=80,null=True)
    complemento = models.CharField(max_length=80,null=True)
    cliente = models.OneToOneField(Cliente, blank=True, null=True, on_delete=models.CASCADE)
