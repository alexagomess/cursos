'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

lista = list()
dados = list()
cont = menor = maior = 0
lista_menor = []
lista_maior = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso(kg): ')))
    lista.append(dados[:])
    dados.clear()

    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('\nDeseja continuar?[S/N] ')).upper()[0]
    if resposta == 'N':
        break

for pessoa in lista:
    if cont == 0:
        menor = pessoa[1]
        maior = pessoa[1]
        cont += 1
    else:
        if pessoa[1] < menor:
            menor = pessoa[1]
        if pessoa[1] > maior:
            maior = pessoa[1]

for pessoa in lista:
    if menor == pessoa[1]:
        lista_menor.append(pessoa[0])
    if maior == pessoa[1]:
        lista_maior.append(pessoa[0])

print(f'\nForam cadastradas {len(lista)} pessoas.')
print(f'O MENOR peso foi de {menor:.1f} kg. Peso de {lista_menor}')
print(f'O MAIOR peso foi {maior:.1f} kg. Peso de {lista_maior}\n')
