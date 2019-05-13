from django.forms import ModelForm
from .models import Endereco

class FormEndereco(ModelForm):


    class Meta:
        model = Endereco
        fields = ['logradouro','numero','bairro','complemento']




