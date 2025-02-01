from django.shortcuts import render, redirect

from .models import Pedido
from produto.models import *

from .utilidades import preco_total

def carrinho(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    preco_total_pedido = preco_total(pedido)
    context = {"itens_pedido":itens_pedido, "pedido":pedido, "preco_total_pedido":preco_total_pedido}
    return render(request, 'carrinho.html', context)

def adicionar_carrinho(request, id_carrinho):
    if request.method == "POST" and id_carrinho:
        dados = request.POST.dict()
        tamanho = dados.get('tamanho')
        id_cor = dados.get('cor')
        if request.user.is_authenticated:
            cliente = request.user.cliente
        else:
            return redirect('carrinho')
        pedido,criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
        item_estoque = ItemEstoque.objects.get(produto__id=id_carrinho, tamanho=tamanho, cor__id=id_cor)
        item_pedido, criado = ItensPedido.objects.get_or_create(item_estoque=item_estoque, pedido=pedido)
        item_pedido.quantidade += 1
        item_pedido.save()
        return redirect('carrinho')
    else:
        return redirect('loja')
