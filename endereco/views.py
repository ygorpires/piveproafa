from django.shortcuts import render,redirect,get_object_or_404

from .models import Endereco
from .forms import FormEndereco

def create_endereco(request):
    form = FormEndereco(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'endereco_.html', {'form': form})



