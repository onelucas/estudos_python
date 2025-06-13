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
    
class Autor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=100)
    idade = models.PositiveIntegerField('Idade')

    def __str__(self):
        return self.nome