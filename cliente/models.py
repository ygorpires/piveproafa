from django.db import models
from django.conf import settings


class Cliente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    nome=models.CharField(max_length=100)
    sobrenome=models.CharField(max_length=100)
    cpf_cnpj=models.CharField(max_length=25)
    email= models.EmailField()
    assinaturas = models.ManyToManyField(Assinatura, blank=False)
    endereco = models.OneToOneField(Endereco, null=False, blank=False, on_delete=models.CASCADE)



    def __str__(self):
        return self.nome + ' ' + self.sobrenome
