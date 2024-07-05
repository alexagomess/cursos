""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se aliastar no serviço militar;
-  Se é a hora de se alistar;
-  Se já passou do tempo do alistamento;
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo """

from datetime import date

sexo = str(input('\nQual seu sexo? \nDigite "M" para mulher e "H" para homem: ')).strip().lower()

if sexo == 'h':
    data_nascimento = int(input('\nDigite o ano do seu nascimento: (YYYY) '))

    data_atual = date.today().year
    diferenca_anos = data_atual - data_nascimento

    if diferenca_anos < 18:
        print(f'\nVocê ainda irá se alistar. Faltam {18-diferenca_anos} anos para o alistamento.')
    elif diferenca_anos == 18:
        print(f'\nVocê tem {diferenca_anos} anos. Está na hora do seu alistamento!')
    else:
        print(f'\nVocê já se alistou. Já se passaram {diferenca_anos-18} anos desde o alistamento.')
elif sexo == 'm':
    print('\nNesse programa apenas HOMENS se alistam. Programa encerrado.')
else:
    print('\nVocê NÃO digitou uma opção válida! Programa encerrado.')
