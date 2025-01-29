import operator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
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
