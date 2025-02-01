from django.shortcuts import render, redirect

from .models import Pedido
from produto.models import ItensPedido

def carrinho(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False) #verificando se existe pedido, se não tiver vai criar um pedido vazio, e retornar duas informações
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    context = {"itens_pedido":itens_pedido, "pedido":pedido}
    return render(request, 'carrinho.html', context)

def adicionar_carrinho(request, id_carrinho):
    if request.method == "POST" and id_carrinho:
        dados = request.POST.dict()
        tamanho = dados.get('tamanho')
        id_cor = dados.get('cor')
        print(tamanho)
        print(id_cor)
        return redirect('loja')
    else:
        return redirect('loja')
