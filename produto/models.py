from django.db import models


LISTA_CATEGORIA = (
    ('roupas_masculinas', 'Roupas Masculinas'),
    ('roupas_femininas', 'Roupas Femininas'),
    ('calcados', 'Calçados'),
    ('livros', 'Livros'),
    ('games', 'Games'),
    ('celulares', 'Celulares'),
    ('informática', 'Informática'),
    ('moveis', 'Móveis'),
)

LISTA_TAMANHO = (
    ('pp', 'PP'),
    ('P', 'P'),
    ('m', 'M'),
    ('g', 'G'),
    ('gg', 'GG'),
)

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(max_length=10000, blank=True, null=True)
    preco = models.DecimalField(max_digits=100, decimal_places=2)
    imagem = models.ImageField(upload_to='thumb_img')
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tamanho = models.CharField(max_length=30, choices=LISTA_TAMANHO, blank=True)
    data = models.DateTimeField(auto_now_add = True)
    vendido = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return f"Nome: {self.titulo} - Preço: {self.preco} - Tamanho: {self.tamanho}"
