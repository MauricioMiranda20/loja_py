README: Ajuste de Preços de Produtos com Python

Este projeto demonstra como usar funções Python para manipular dados de produtos e aplicar regras de reajuste de preços de forma dinâmica, utilizando conceitos como map, partial do módulo functools, e funções anônimas (lambda).

Funcionalidades

Manipulação de Dados de Produtos:

A lista de produtos contém dicionários com o nome e o preço de cada produto.

Os preços podem ser ajustados com base em condições específicas.

Ajuste Dinâmico de Preços:

Produtos com preços acima de R$100,00 recebem um reajuste percentual.

Produtos com preços abaixo ou igual a R$100,00 permanecem inalterados.

Exibição dos Resultados:

Exibe a lista original e a lista ajustada no terminal, com uma formatação clara.

Tecnologias Utilizadas

Python: Linguagem de programação principal.

functools.partial: Para criar funções com argumentos pré-definidos.

map: Para aplicar funções a elementos de uma lista de maneira funcional.

Estrutura do Código

Lista de Produtos: Representada como uma lista de dicionários.

Função de Ajuste:

valor_acima_de_cem(valor, porcentagem): Aplica o ajuste de preços.

Função Parcial:

Utiliza functools.partial para fixar a porcentagem como parâmetro.

Transformação de Preços:

A função map aplica a transformação de forma funcional aos produtos.

Exibição:

A função print_ite formata e exibe os resultados.

Como Usar

Clone este repositório:

git clone <URL-DO-REPOSITÓRIO>

Navegue até a pasta do projeto:

cd pasta-projeto

Execute o script Python:

python ajustar_precos.py

Exemplo de Saída

Entrada:

produtos = [
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 3', 'preco': 10.11},
]

Configuração:

Porcentagem de ajuste: 10% (0.10).

Saída:

{'nome': 'Produto 1', 'preco': 22.32}
{'nome': 'Produto 2', 'preco': 116.46}
{'nome': 'Produto 3', 'preco': 10.11}

Personalização

Alterar Porcentagem: Modifique o valor fixado na função partial para mudar a porcentagem de reajuste.

Condições de Ajuste: Ajuste a lógica dentro da função valor_acima_de_cem para criar novas regras.

Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções de bugs ou novas funcionalidades. 🚀

Licença

Este projeto está licenciado sob a MIT License.

