from django.urls import path
from .views import *


urlpatterns = [
    path('', carrinho, name='carrinho'),
    path('adicionarcarrinho/<int:id_carrinho>/', adicionar_carrinho, name='adicionar_carrinho'),

]
