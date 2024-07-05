"""Crie um programa que faça o computador jogar jokenpô com você."""

from random import randint

print('\n')
print('-'*49)
print('-'*20, 'JOKENPÔ', '-'*20)
print('-'*49)

print('Computador: Vamos jogar jokenpô?')
print('\nVocê tem essas opções: ')
print('( 1 ) - PEDRA')
print('( 2 ) - PAPEL')
print('( 3 ) - TESOURA')

escolha_computador = randint(1,3)
escolha_usuario = int(input('\nDigite sua escolha: '))
print('-'*49)
print('\n')

if escolha_usuario == 1:
    if escolha_computador == 1:
        print('Houve um EMPTATE! O computador escolheu PEDRA e você PEDRA.')
    elif escolha_computador == 2:
        print('Você PERDEU! O computador escolheu PAPEL e você PEDRA.')
    elif escolha_computador == 3:
        print('Você GANHOU! O computador escolheu TESOURA e você PEDRA.')
elif escolha_usuario == 2:
    if escolha_computador == 1:
        print('Você GANHOU! O computador escolheu PEDRA e você PAPEL.')
    elif escolha_computador == 2:
        print('Houve um EMPTATE! O computador escolheu PAPEL e você PAPEL.')
    elif escolha_computador == 3:
        print('Você PERDEU! O computador escolheu TESOURA e você PAPEL.')
elif escolha_usuario == 3:
    if escolha_computador == 1:
        print('Você PERDEU! O computador escolheu PEDRA e você TESOURA.')
    elif escolha_computador == 2:
        print('Você GANHOU! O computador escolheu PAPEL e você TESOURA.')
    elif escolha_computador == 3:
        print('Houve um EMPTATE! O computador escolheu TESOURA e você TESOURA.')
else:
    print('Você NÃO digitou uma opção válida! Programa encerrado.')
print('\n')
print('-'*49)

