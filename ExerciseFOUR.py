"""
UNIR LISTAS
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem. use todos os valores da menor lista.

Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']

Resultado:
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

# JEITO LONGO:
from itertools import zip_longest
print('')


def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))  # Também tem o max, que diz qual dos numeros é maior
    return [(l1[i], l2[i]) for i in range(intervalo)]


lista_A = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_B = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista_A, lista_B))
print('\n')

# JEITO CURTO(1):

print(list(zip(lista_A, lista_B)))  # caso já saibas qual das listas é a maior lista e a menor.
print('\n')
# JEITO CURTO(2):
print(list(zip_longest(lista_A, lista_B, fillvalue='SEM CIDADE')))  # usa a lista maior, o fillvalue é executado quando encontra uma posicao vazia
