from django.db import models
from django.contrib.auth.models import User



class Cliente(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    nome=models.CharField(max_length=100)
    sobrenome=models.CharField(max_length=100)
    cpf=models.CharField(max_length=25)
    email= models.EmailField()

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
