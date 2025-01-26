from produto.models import Categoria

def categorias_disponiveis(request):
    categorias = Categoria.objects.all
    return {'categorias':categorias}
