from produto.models import ItensPedido


def preco_total(pedido):
    itens_pedido = ItensPedido.objects.filter(pedido__id=pedido.id)
    preco = sum([ item.preco_total for item in itens_pedido])
    return preco
