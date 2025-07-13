from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'

class DetalheProduto(ListView):
    pass

class AdicionarAoCarrinho(ListView):
    pass

class RemoverdoCarrinho(ListView):
    pass

class Carrinho(ListView):
    pass

class Finalizar(ListView):
    pass