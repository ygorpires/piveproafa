from django.db import models
from cooperativa.models import Cooperativa

class Produto(models.Model):
    nome = models.CharField(max_length=80)
    tipo = models.CharField(max_length=25)
    un_medida = models.CharField(max_length=2)
    foto = models.ImageField(upload_to='img_produtos', null=True, blank=True)

    def __str__(self):
        return self.nome

class Producao(models.Model):
    cooperativa= models.OneToOneField(Cooperativa,null=False,blank=False,on_delete= models.PROTECT)
    produto=models.OneToOneField(Produto,null=False,blank=False,on_delete= models.PROTECT)
    preco=models.DecimalField(max_digits=3,decimal_places=2)
    quantidade= models.DecimalField(max_digits=4,decimal_places=3)
