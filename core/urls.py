from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),
    path('produto/', include('produto.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('usuario/', include('usuario.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
