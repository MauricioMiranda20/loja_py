produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novo_produto = [{**produto,'preco': produto['preco'] * 0.10 + produto['preco']}
                for produto in produtos
                ]

for chave in novo_produto:
    print(f"{chave['nome']} : R${chave['preco']:.2f}")