from functools import partial

def print_ite(iterator):
    print(*list(iterator),sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def valor_acima_de_cem(valor,porcentage):
    if valor > 100:
        return f'{round(valor*porcentage,2)+valor:.2f}'
    return f'{valor:.2f}'

valor_preco = partial(valor_acima_de_cem,porcentage=0.05)

def mudar_preco_acima_de_cen(produto):
    return {**produto,'preco':valor_preco(produto['preco'])}

valor = list(map(mudar_preco_acima_de_cen,produtos))

print_ite(valor)
