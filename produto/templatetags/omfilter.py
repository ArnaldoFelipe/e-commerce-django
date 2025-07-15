from django import template

register = template.Library()

@register.filter
def formatar_preco(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')