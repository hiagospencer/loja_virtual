from ..models import Produto

def categorias_produtos(categoria):
    categorias = Produto.objects.filter(categoria='roupa')
    return categorias

def quantidade_produtos_tamanhos(tamanho):
    pass
