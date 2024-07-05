# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
## O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
from time import sleep

pc = random.randint(0,5)
user = int(input('Adivinhe qual número o computador pensou: '))
print('Processando....')
sleep(2)

if user == pc:
    print('Você acertou! O computador pensou {}.'.format(pc))
else:
    print('Você errou! O computador pensou {} e você digitou {}.'.format(pc, user))
