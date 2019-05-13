
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from home import urls as home_urls
from producao import urls as producao_urls
from cliente import urls as cliente_urls
from assinatura import urls as assinatura_urls
from endereco import urls as endereco_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(home_urls)),
    path('producao/',include(producao_urls)),
    path('clientes/',include(cliente_urls)),
    path('assinatura/',include(assinatura_urls)),
    path('endereco/',include(endereco_urls)),
    path('login/',auth_views.LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
