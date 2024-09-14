'''Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como valor monetário formatado.'''

import moeda

num = float(input('Digite um preço: R$ '))
print(f'\nO dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O preço de {moeda.moeda(num)} com acréscimo de 10% é {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'O preço de {moeda.moeda(num) } menos 10% é {moeda.moeda(moeda.diminuir(num, 10))}')
