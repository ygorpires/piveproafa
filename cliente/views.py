from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Cliente
from endereco.models import Endereco
from .forms import FormCliente
from endereco.forms import FormEndereco

@login_required
def create_cliente(request):

   form = FormCliente(request.POST or None, request.FILES or None)
   formEnd = FormEndereco(request.POST or None, request.FILES or None)
   if form.is_valid():
        cli = form.save(commit=False)
        cli.usuario = request.user
        cli.save()
        end = formEnd.save(commit=False)
        end.cliente = form.instance
        end.save()

   return render(request,"create_cliente.html",{"form":form,"formEnd":formEnd})


def update_cliente(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('detalhe_cliente',id = id)
    return render(request,"update_cliente.html",{"form":form})

def update_endereco(request,id):
    endereco = get_object_or_404(Endereco,pk=id)
    form = FormEndereco(request.POST or None, request.FILES or None, instance=endereco)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update_endereco.html',{"form":form})

def create_user(request):
    form = UserCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(create_cliente)

    return render(request,"create_user.html",{"form":form})

def detalhe_cliente(request,id):
    cli = Cliente.objects.get(pk=id)

    endereco = Endereco.objects.filter(cliente=cli.id).select_related()

    return render(request,"detalhe_cliente.html",{"endereco":endereco})





def list_cliente (request):
    #cliente = get_object_or_404(Cliente,pk=id)
    #cliente = Cliente.objects.filter(id=id)
    cliente = Cliente.objects.all()
    return render(request,"list_cliente.html",{'cliente':cliente})