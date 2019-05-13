from django.urls import path
from .views import create_cliente,list_cliente,create_user,detalhe_cliente,update_cliente,update_endereco

urlpatterns = [
    path('cadastro/', create_cliente, name='create_cliente'),
    path('registro/', create_user, name='create_user'),
    path('detalhe/<int:id>/', detalhe_cliente, name='detalhe_cliente'),
    path('update_cliente/<int:id>/', update_cliente, name='update_cliente'),
    path('update_endereco/<int:id>/', update_endereco, name='update_endereco'),
    path('listar_cliente/', list_cliente, name='list_cliente')
]

