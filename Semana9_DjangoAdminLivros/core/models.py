from django.db import models

class Livro(models.Model):
    titulo = models.CharField('Título', max_length=100)
    genero = models.CharField('Genero', max_length=60, null=True)
    data_publicacao = models.DateField('Data de publicação', null=True)
    numero_paginas = models.PositiveIntegerField('Páginas')
    estoque = models.PositiveIntegerField('Quantidade', null=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    autor = models.CharField('Autor', max_length=100, null=True)

    def __str__(self):
        return self.titulo