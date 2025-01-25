from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from produto.models import Produto, Categoria


def homepage(request):
    produtos_recentes = Produto.objects.filter(destaque=False).order_by('-data')[:12]
    produtos_destaque = Produto.objects.filter(destaque=True).order_by('-data')[:12]

    context = {"produtos_recentes":produtos_recentes, "produtos_destaque":produtos_destaque}
    return render(request, 'index.html', context)

def detalhes_produtos(request, id_produto):
    # produto = Produto.objects.get(id=id_produto)
    produto = get_object_or_404(Produto, id=id_produto)

    print(produto)
    context = {'produto':produto}
    return render(request,'detalhes.html', context)


def loja(request):
    return render(request, 'loja.html')
