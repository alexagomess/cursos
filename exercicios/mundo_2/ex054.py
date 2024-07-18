'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
Aqui, a maioridade é atingida aos 21 anos.'''

from datetime import date

count_maior_idade = 0
count_menor_idade = 0
ano_atual = date.today().year

for i in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da pessoa {i} [YYYY]: '))

    verifica_maioridade = ano_atual - ano_nascimento

    if verifica_maioridade > 21:
        count_maior_idade = count_maior_idade + 1
    else:
        count_menor_idade = count_menor_idade + 1

print(f'\nA quantidade de pessoas que já atingiram a maioridade é {count_maior_idade} e que NÃO atingiram é {count_menor_idade}.')
