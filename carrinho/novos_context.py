from .models import Pedido
from produto.models import ItensPedido


def carrinho(request):
    quantidade_produtos_carrinho = 0
    if request.user.is_authenticated:
        cliente = request.user.cliente
    else:
        pass

    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False) #verificando se existe pedido, se não tiver vai criar um pedido vazio, e retornar duas informações
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)

    quantidade_produtos_carrinho = len(itens_pedido)
    return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}
