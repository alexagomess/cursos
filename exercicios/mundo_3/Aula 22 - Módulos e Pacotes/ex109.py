'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda() desenvolvida no desafio 108.'''

import moeda

num = float(input('Digite um preço: R$ '))
print(f'\nO dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O preço de {moeda.moeda(num)} com acréscimo de 10% é {moeda.aumentar(num, 10, True)}')
print(f'O preço de {moeda.moeda(num)} menos 10% é {moeda.diminuir(num, 10, True)}')
