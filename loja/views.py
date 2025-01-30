from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Q

from produto.models import *


def homepage(request):
    produtos_recentes = Produto.objects.filter(destaque=False).order_by('-data')[:8]
    produtos_destaque = Produto.objects.filter(destaque=True).order_by('-data')[:8]

    context = {"produtos_recentes":produtos_recentes, "produtos_destaque":produtos_destaque}
    return render(request, 'index.html', context)

def detalhes_produtos(request, id_produto, id_cor=None):
    tem_estoque = False
    tem_cor = False
    cores = {}
    tamanhos = {}
    todos_produtos = Produto.objects.all().order_by('-data')
    produto = get_object_or_404(Produto, id=id_produto)
    item_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)
    for item in item_estoque:
        if item.cor:
            tem_cor = True
    if len(item_estoque) > 0:
        tem_estoque = True
        cores = {item.cor for item in item_estoque}
    context = {
        'produto':produto, "todos_produtos":todos_produtos, "item_estoque":item_estoque, "tem_estoque":tem_estoque, "cores":cores,  "tem_cor":tem_cor,
        }
    return render(request,'detalhes.html', context)


def loja(request, nome_categoria=None):
    produtos = Produto.objects.all()
    if nome_categoria:
        produtos = produtos.filter(categoria__nome=nome_categoria)
    precos = request.GET.getlist('precos')
    if precos:
        queries = Q()
        for preco in precos:
            if preco == "1":
                queries |= Q(preco__lte=100)
            elif preco == "2":
                queries |= Q(preco__gt=100, preco__lte=300)
            elif preco == "3":
                queries |= Q(preco__gt=300, preco__lte=500)
            elif preco == "4":
                queries |= Q(preco__gt=500, preco__lte=1000)
            elif preco == "5":
                queries |= Q(preco__gt=1000)
        produtos = produtos.filter(queries)
    paginator = Paginator(produtos.order_by('-data'), 12)  # 6 produtos por página
    page_number = request.GET.get('page')  # Captura a página atual
    page_obj = paginator.get_page(page_number)  # Obtém os produtos da página

    return render(request, 'loja.html', {
        'produtos': page_obj,
        'precos': precos,
        'nome_categoria': nome_categoria  # Para manter o contexto da categoria
    })
