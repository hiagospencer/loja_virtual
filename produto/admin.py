from django.contrib import admin
from .models import *


class ProdutoImagemInline(admin.TabularInline):
    model = ProdutoImagem
    extra = 1  # Número de imagens adicionais que aparecem para upload.


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'categoria')
    inlines = [ProdutoImagemInline]

@admin.register(ItemEstoque)
class ItemEstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tamanho', 'cor')


admin.site.register(Categoria)
admin.site.register(Cor)
