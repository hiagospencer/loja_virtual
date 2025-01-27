from django.shortcuts import get_object_or_404, render

from produto.models import *


def produto_htmx(request, id_produto, id_cor):
    tem_tamanho = False
    produto = get_object_or_404(Produto, id=id_produto)
    item_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)
    for item in item_estoque:
        if item.tamanho:
            tem_tamanho = True
        if id_cor:
            itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0, cor__id=id_cor)
            tamanhos = {item.tamanho for item in itens_estoque}
    context = {"tamanhos":tamanhos, "tem_tamanho":tem_tamanho}
    return render(request, 'templates_htmx/mostrar_tamanhos.html', context)
