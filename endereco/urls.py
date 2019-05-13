from django.urls import path
from .views import create_endereco

urlpatterns = [
    path('criar_endereco/', create_endereco, name='create_endereco')
]
