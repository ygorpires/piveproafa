from django.urls import path
from .views import producao_list

urlpatterns = [
    path('list/', producao_list,name='producao_list')
]