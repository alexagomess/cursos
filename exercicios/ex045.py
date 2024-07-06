"""Crie um programa que faça o computador jogar jokenpô com você."""

from random import randint
from time import sleep

print('\n')
print('-'*49)
print('-'*20, 'JOKENPÔ', '-'*20)
print('-'*49)

print('Computador: Vamos jogar jokenpô?')
print('\nVocê tem essas opções: ')
print('( 0 ) - PEDRA')
print('( 1 ) - PAPEL')
print('( 2 ) - TESOURA')

escolha_computador = randint(0,2)
escolha_usuario = int(input('\nDigite sua escolha: '))
print('-'*49)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
sleep(1)
if escolha_usuario == 0:
    if escolha_computador == 0:
        print('Houve um EMPATE! \nO computador escolheu PEDRA e você PEDRA.')
    elif escolha_computador == 1:
        print('Você PERDEU! \nO computador escolheu PAPEL e você PEDRA.')
    elif escolha_computador == 2:
        print('Você GANHOU! \nO computador escolheu TESOURA e você PEDRA.')
elif escolha_usuario == 1:
    if escolha_computador == 0:
        print('Você GANHOU! \nO computador escolheu PEDRA e você PAPEL.')
    elif escolha_computador == 1:
        print('Houve um EMPATE! \nO computador escolheu PAPEL e você PAPEL.')
    elif escolha_computador == 2:
        print('Você PERDEU! \nO computador escolheu TESOURA e você PAPEL.')
elif escolha_usuario == 2:
    if escolha_computador == 0:
        print('Você PERDEU! \nO computador escolheu PEDRA e você TESOURA.')
    elif escolha_computador == 1:
        print('Você GANHOU! \nO computador escolheu PAPEL e você TESOURA.')
    elif escolha_computador == 2:
        print('Houve um EMPATE! \nO computador escolheu TESOURA e você TESOURA.')
else:
    print('Você NÃO digitou uma opção válida! Programa encerrado.')
print('-'*49)

