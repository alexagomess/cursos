'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

lista = []
lista_temp = []
repeticoes = 0

print('-'*35)
print(f'{"MEGA SENA":^35}')
print('-'*35)

qtd = int(input('\nQuantos jogos você quer sortear? '))
print('\n')

print('-'*35)
print(f'{f"Sorteando {qtd} jogo(s)":^35}')
print('-'*35)

while repeticoes != qtd:
    cont = 0
    while True:
        numeros_aleatorios = randint(1, 60)
        if numeros_aleatorios not in lista_temp:
            lista_temp.append(numeros_aleatorios)
            cont += 1
        if cont >= 6:
            break
    lista_temp.sort()
    lista.append(lista_temp[:])
    lista_temp.clear()
    repeticoes += 1

qtd_jogo = 1
for jogo in lista:
    sleep(1)
    print(f'Jogo {qtd_jogo}: {jogo}')
    qtd_jogo += 1
print('-'*35)
print(f'{"Boa sorte!!":^35}')
print('-'*35)
