from django.urls import path
from .views import *
from .htmx_views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('loja/', loja, name='loja'),
    path('loja/<str:nome_categoria>/', loja, name='loja'),
    path('detalhes-produtos/<int:id_produto>/', detalhes_produtos, name='detalhes_produtos'),
    path('detalhes-produtos/<int:id_produto>/<int:id_cor>/', detalhes_produtos, name='detalhes_produtos'),
]


htmx_urlpatterns = [
     path('detalhes/<int:id_produto>/<int:id_cor>/', produto_htmx, name='produto_htmx'),
]

urlpatterns += htmx_urlpatterns
