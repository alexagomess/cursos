'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

dicionario = {}
dicionario['Nome'] = str(input('Nome: ')).strip()
dicionario['Média'] = float(input(f'Média de {dicionario['Nome']}: '))
if dicionario['Média'] >= 7.0:
    dicionario['Situação'] = 'Aprovado'
elif dicionario['Média'] >= 5:
    dicionario['Situação'] = 'Em recuperação'
else:
    dicionario['Situação'] = 'Reprovado'
print('-'*35)
for k, v in dicionario.items():
    print(f'{k} é igual a {v}')
