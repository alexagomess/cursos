"""Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

print("=-"*15)
print("CADASTRO DE PESSOAS")
print("=-"*15)

pessoas_maior_18 = qtd_homens = qtd_mulheres_menos_20 = 0

while True:
    idade = int(input('\nDigite a idade da pessoa: '))

    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        pessoas_maior_18 += 1
    if sexo == 'M':
        qtd_homens += 1
    if sexo == 'F' and idade <= 20:
        qtd_mulheres_menos_20 += 1

    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
    
print(f'\nTem {pessoas_maior_18} pessoas com maior de 18 anos.')
print(f'{qtd_homens} homens foram cadastrados.')
print(f'{qtd_mulheres_menos_20} mulheres tem menos de 20 anos.')
