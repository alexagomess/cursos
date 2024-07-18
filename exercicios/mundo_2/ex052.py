'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

# from sympy import isprime

# num = int(input('Digite um número inteiro: '))

# if isprime(num):
#     print(f'\nO número {num} É número primo.')
# else:
#     print(f'\nO número {num} NÃO é número primo.')

num = int(input('Digite um número inteiro: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('É número primo.')
else:
    print('Não é número primo.')
