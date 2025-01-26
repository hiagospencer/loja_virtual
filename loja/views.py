from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from produto.models import *


def homepage(request):
    produtos_recentes = Produto.objects.filter(destaque=False).order_by('-data')[:8]
    produtos_destaque = Produto.objects.filter(destaque=True).order_by('-data')[:8]

    context = {"produtos_recentes":produtos_recentes, "produtos_destaque":produtos_destaque}
    return render(request, 'index.html', context)

def detalhes_produtos(request, id_produto):
    todos_produtos = Produto.objects.all().order_by('-data')
    produto = get_object_or_404(Produto, id=id_produto)
    item_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)
    if len(item_estoque) > 0:
        tem_estoque = True
        cores = {item.cor for item in item_estoque}
    else:
        tem_estoque = False
    context = {'produto':produto, "todos_produtos":todos_produtos, "item_estoque":item_estoque, "tem_estoque":tem_estoque, "cores":cores}
    return render(request,'detalhes.html', context)


def loja(request, nome_categoria=None):
    if nome_categoria:
        produtos = Produto.objects.filter(categoria__nome=nome_categoria).order_by('-data')[:15]
    else:
        produtos = Produto.objects.all().order_by('-data')[:15]
    context = {"produtos":produtos}
    return render(request, 'loja.html', context)
