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

    def featured_image(self):
        """Retorna a imagem marcada como destaque ou a primeira."""
        return self.imagem.filter(em_destaque=True).first() or self.imagem.first()

    def __str__(self):
        return f"Nome: {self.titulo} - Preço: {self.preco} - Tamanho: {self.tamanho}"



class ProdutoImagem(models.Model):
    produto = models.ForeignKey(Produto, related_name='images', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='thumb_img')
    em_destaque = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """Garante que apenas uma imagem seja destacada por produto."""
        if self.em_destaque:
            ProdutoImagem.objects.filter(produto=self.produto).update(em_destaque=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Imagen de {self.produto.titulo}"
