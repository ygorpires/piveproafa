from django.urls import path
from .views import novo_assinatura


urlpatterns = [
    path('novo/', novo_assinatura ,name='novo_assinatura'),
]