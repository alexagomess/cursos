"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date

ano_atual = date.today().year

dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano nascimento: '))
dicionario['Idade'] = ano_atual - ano_nascimento
dicionario['CTPS'] = int(input('ID carteira de trabalho (0 não tem): '))
if dicionario['CTPS'] != 0:
    dicionario['Ano contratação'] = int(input('Ano de contratação: '))
    dicionario['Salário'] = float(input('Salário: R$'))
    if ano_atual - dicionario['Ano contratação'] < 35:
        dicionario['Aponsentadoria'] = (dicionario['Ano contratação'] + 35) - ano_nascimento
    else:
        dicionario['Aponsentadoria'] = 'Já está aposentado'
print('-='*35)
print(dicionario)

for k, v in dicionario.items():
    print(f'{k} tem o valor: {v}')
