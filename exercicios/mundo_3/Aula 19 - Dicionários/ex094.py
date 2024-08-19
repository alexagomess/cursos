'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dicionario = {}
lista = []
soma = 0

while True:
    dicionario['Nome'] = str(input('Nome: ')).strip()
    while True:
        dicionario['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if dicionario['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    dicionario['Idade'] = int(input('Idade: '))
    lista.append(dicionario.copy())
    while True:
        resposta = str(input('Deseja continuar[S/N]? ')).upper()
        if resposta in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
        print('-='*25)
    if resposta == 'N':
        break
print(lista)
print('-='*25)
print(f'- O grupo tem {len(lista)} pessoas.')

for dic in lista:
    soma += dic["Idade"]
media = soma / len(lista)
print(f'- A média de idade é {media:.1f} anos.')

lista_mulheres = []
for dic in lista:
    if 'F' in dic['Sexo']:
        if dic['Sexo'] == 'F':
            lista_mulheres.append(dic['Nome'])
print(f'- As mulheres cadastradas foram: {lista_mulheres}')

print('- As pessoas acima da média são: ')
for dic in lista:
    if dic["Idade"] >= media:
        print(f'    - Nome = {dic['Nome']}; sexo = {dic['Sexo']}; idade = {dic['Idade']}')
print('Programa encerrado!')
