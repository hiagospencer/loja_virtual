from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('detalhes-produtos/<int:id_produto>/', detalhes_produtos, name='detalhes_produtos'),
    path('loja/', loja, name='loja'),
    path('loja/<str:nome_categoria>/', loja, name='loja')
]
