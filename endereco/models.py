from django.db import models

# Create your models here.
class Endereco(models.Model):
    logradouro = models.CharField(max_length=80)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=80)
    telefone = models.CharField(max_length=30)