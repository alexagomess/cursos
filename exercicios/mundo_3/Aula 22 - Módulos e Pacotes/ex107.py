'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções
'''


import moeda

num = int(input('Digite um preço: R$ '))
print(f'\nO dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O preço de {num} com acréscimo de 10% é {moeda.aumentar(num, 10)}')
print(f'O preço de {num} menos 10% é {moeda.diminuir(num, 10)}')
