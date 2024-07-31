"""Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint

print("=-"*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*15)

cont = 0

while True:
    num_user = int(input('\nDigite um valor: '))
    num_pc = randint(0,10)
    soma = num_user + num_pc
    opt_user = ' '

    while opt_user not in 'PpIi':
        opt_user = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]

    if opt_user == 'P' and soma % 2 != 0:
        print(f'Você PERDEU! Você jogou {num_user} e o computador {num_pc}. Total de {soma} deu ÍMPAR.')
        break
    if opt_user == 'P' and soma % 2 == 0:
        print(f'Você GANHOU! Você jogou {num_user} e o computador {num_pc}. Total de {soma} deu PAR.')
        print('\nVamos jogar novamente...')
        print("=-"*15)
    if opt_user == 'I' and soma % 2 == 0:
        print(f'Você PERDEU! Você jogou {num_user} e o computador {num_pc}. Total de {soma} deu PAR.')
        break
    if opt_user == 'I' and soma % 2 != 0:
        print(f'Você GANHOU! Você jogou {num_user} e o computador {num_pc}. Total de {soma} deu ÍMPAR.')
        print('\nVamos jogar novamente...')
        print("=-"*15)
    cont =+ 1

print("=-"*15)
print(f'\nGAME OVER! Você venceu {cont} vezes.')

