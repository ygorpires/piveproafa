from django.shortcuts import render
from .models import Producao

# Create your views here.

# Create your views here.
def producao_list(request):
    producoes= Producao.objects.all()
    return render(request,'list.html',{'producoes':producoes})