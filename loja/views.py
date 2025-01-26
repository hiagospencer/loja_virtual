from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from produto.models import Produto, Categoria


def homepage(request):
    produtos_recentes = Produto.objects.filter(destaque=False).order_by('-data')[:12]
    produtos_destaque = Produto.objects.filter(destaque=True).order_by('-data')[:12]

    context = {"produtos_recentes":produtos_recentes, "produtos_destaque":produtos_destaque}
    return render(request, 'index.html', context)

def detalhes_produtos(request, id_produto):
    todos_produtos = Produto.objects.all().order_by('-data')
    produto = get_object_or_404(Produto, id=id_produto)

    context = {'produto':produto, "todos_produtos":todos_produtos}
    return render(request,'detalhes.html', context)


def loja(request, nome_categoria=None):
    produtos = Produto.objects.filter(categoria__nome=nome_categoria).order_by('-data')[:15]
    print(nome_categoria)
    context = {"produtos":produtos}
    return render(request, 'loja.html', context)
