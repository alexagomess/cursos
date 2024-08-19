'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

dicionario = dict()
dicionario_ordenado = list()

print('Valores sorteados:')
for c in range(1, 5):
    dicionario[f"jogador{c}"] = randint(1, 6)
    print(f'O jogador {c} tirou {dicionario[f"jogador{c}"]}')
    sleep(1)

print('\nRanking dos jogadores:')
dicionario_ordenado = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for indice, valor in enumerate(dicionario_ordenado):
    sleep(1)
    print(f'{indice+1} lugar: {valor[0]} com {valor[1]}.')
