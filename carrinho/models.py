from django.db import models
from produto.models import ItensPedido
from usuario.models import Cliente, Endereco

# Create your models here.
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_trasacao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True)

    @property
    def preco_total(self):
        itens_pedido = ItensPedido.objects.filter(pedido__id=self.id)
        preco = sum([ item.preco_total for item in itens_pedido])
        return preco

    def __str__(self):
        return f'Cliente: {self.cliente.email} - id_pedido: {self.id} - Finalizado: {self.finalizado}'
