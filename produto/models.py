from django.db import models

LISTA_CATEGORIA = (
    ('roupas', 'Roupas'),
    ('calcados', 'Calçados'),
    ('livros', 'Livros'),
    ('games', 'Games'),
    ('celulares', 'Celulares'),
    ('informática', 'Informática'),
    ('moveis', 'Móveis'),

)

class Produto(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=1000, blank=True, null=True)
    preco = models.DecimalField(max_digits=100, decimal_places=2)
    imagem = models.ImageField(upload_to='thumb_img')
    categoria = models.CharField(max_length=30, choices=LISTA_CATEGORIA)
    data = models.DateTimeField(auto_now_add = True)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return f"Nome: {self.titulo} - Preço: {self.preco} - Vendido: {self.vendido}"
