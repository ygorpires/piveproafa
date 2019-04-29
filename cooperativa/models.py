from django.db import models
from django.conf import settings
from endereco.models import Endereco

# Create your models here.

class Cooperativa(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    razao_social=models.CharField(max_length=100)
    nome_fantasia=models.CharField(max_length=100)
    aprovado=models.NullBooleanField()
    endereco = models.OneToOneField(Endereco, null=False, blank=False, on_delete=models.CASCADE)