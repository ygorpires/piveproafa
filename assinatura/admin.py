from django.contrib import admin
from .models import Assinatura,TipoPagamento,Pacote

admin.site.register(Assinatura)
admin.site.register(Pacote)
admin.site.register(TipoPagamento)

