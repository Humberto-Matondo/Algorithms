"""
Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)
Ordene os produtos por nome decrescente (do maior para menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
Ordene os produtos por preco crescente (do menor para maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
Ordene os produtos por preco crescente (do menor para maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


produto = [

    {**pro, 'preco': round(pro['preco'] * 1.1, 2)}  # roud(pro['preco']* 1.1, 2) para ter valores apenas com '2' casa decimal
    for pro in copy.deepcopy(produtos)

]

print()
print(*produto, sep=' \n')
print()

dic = copy.deepcopy(sorted(produto, key=lambda item: item['preco']))  # preco vira do menor ao maior
dic_2 = copy.deepcopy(sorted(produto, reverse=True, key=lambda item: item['nome']))  # ordenado pelo nome em ordem decrescente

print('\n COPIA CRESCENTE: \n')
print(*dic, sep='\n')

print('\nCOPIA DECRESCENTE: \n')
print(*dic_2, sep='\n')
