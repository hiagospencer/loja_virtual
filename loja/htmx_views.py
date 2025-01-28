import operator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Q
from functools import reduce

from produto.models import *


def produto_htmx(request, id_produto, id_cor=None):
    tem_estoque = False
    tem_cor = False
    tem_tamanho = False
    cores = {}
    tamanhos = {}
    cor_selecionada = request.GET.get('cor_selecionada')
    if id_cor:
        cor_selecionada = Cor.objects.get(id=id_cor)
    todos_produtos = Produto.objects.all().order_by('-data')
    produto = get_object_or_404(Produto, id=id_produto)
    item_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)
    for item in item_estoque:
        if item.cor:
            tem_cor = True
        if item.tamanho:
            tem_tamanho = True
    if len(item_estoque) > 0:
        tem_estoque = True
        cores = {item.cor for item in item_estoque}
        if id_cor:
            itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0, cor__id=id_cor)
            tamanhos = {item.tamanho for item in itens_estoque}
    context = {
        'produto':produto, "todos_produtos":todos_produtos, "item_estoque":item_estoque, "tem_estoque":tem_estoque, "cores":cores, "tamanhos": tamanhos, "cor_selecionada": cor_selecionada, "tem_cor":tem_cor,"tem_tamanho":tem_tamanho
        }
    return render(request, 'templates_htmx/mostrar_tamanhos.html', context)


def filtrar_produtos(request):
    precos = request.GET.getlist('precos[]')
    produtos = Produto.objects.all()

    # Aplicar filtros de preço
    if precos:
        queries = []
        for preco in precos:
            if preco == "1":
                queries.append(Q(preco__lte=100))
            elif preco == "2":
                queries.append(Q(preco__gt=100, preco__lte=300))
            elif preco == "3":
                queries.append(Q(preco__gt=300, preco__lte=500))
            elif preco == "4":
                queries.append(Q(preco__gt=500, preco__lte=1000))
            elif preco == "5":
                queries.append(Q(preco__gt=1000))
        produtos = produtos.filter(reduce(operator.or_, queries)).order_by('-preco')


    paginator = Paginator(produtos, 2)  # Exibir 5 produtos por página
    page_number = request.GET.get('page', 1)
    produtos_paginados = paginator.get_page(page_number)

    # Renderiza somente os produtos filtrados
    context = {'produtos': produtos_paginados, 'precos_selecionados': precos}
    return render(request, 'templates_htmx/loja_produtos_filtro.html', context)
