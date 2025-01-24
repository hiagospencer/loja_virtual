from django.http import HttpResponse
from django.shortcuts import render

from produto.models import Produto, Categoria


def homepage(request):
    produtos_recentes = Produto.objects.filter(destaque=False).order_by('-data')[:8]
    produtos_destaque = Produto.objects.filter(destaque=True).order_by('-data')[:8]

    context = {"produtos_recentes":produtos_recentes, "produtos_destaque":produtos_destaque}
    return render(request, 'index.html', context)

def loja(request):
    return render(request, 'loja.html')
