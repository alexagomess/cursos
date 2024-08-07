'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

# numeros_aleatorios = tuple(randint(1, 100) for c in range(0,5))
numeros_aleatorios = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

print(f'\nOs números gerados foram: {numeros_aleatorios}')
# print(f'O menor valor da tupla é: {min(numeros_aleatorios)}') #Essa forma é mais simples e mais rápida para saber quem é o menor e maior valor da tupla
# print(f'O maior valor da tupla é: {max(numeros_aleatorios)}') #Essa forma é mais simples e mais rápida para saber quem é o menor e maior valor da tupla

#O formato abaixo envolve lógica para descobrir quem é o menor e maior valor da tupla
for cont in range(0, len(numeros_aleatorios)):
    if cont == 0:
        menor = numeros_aleatorios[cont]
        maior = numeros_aleatorios[cont]
    else:
        if numeros_aleatorios[cont] < menor:
            menor = numeros_aleatorios[cont]
        if numeros_aleatorios[cont] > maior:
            maior = numeros_aleatorios[cont]
    cont += 1
print(f'O MENOR valor é: {menor}')
print(f'O MAIOR valor é: {maior}')
