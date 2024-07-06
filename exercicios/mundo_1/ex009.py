#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numero = int(input('Digite um número inteiro: '))

print('='*10, 'TABUADA DE {}'.format(numero), '='*10)
print('{} * {:2} = {}'.format(numero, 1, numero * 1))
print('{} * {:2} = {}'.format(numero, 2, numero * 2))
print('{} * {:2} = {}'.format(numero, 3, numero * 3))
print('{} * {:2} = {}'.format(numero, 4, numero * 4))
print('{} * {:2} = {}'.format(numero, 5, numero * 5))
print('{} * {:2} = {}'.format(numero, 6, numero * 6))
print('{} * {:2} = {}'.format(numero, 7, numero * 7))
print('{} * {:2} = {}'.format(numero, 8, numero * 8))
print('{} * {:2} = {}'.format(numero, 9, numero * 9))
print('{} * {:2} = {}'.format(numero, 10, numero * 10))
