'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''


lista = []
menor = maior = posmenor = posmaior = 0

for cont in range(0, 5):
    lista.append(int(input('Digite um número: ')))

print('\n')    
for posicao, valor in enumerate(lista):
    if posicao == 0:
        menor = maior = valor
        posmenor = posmaior = posicao
    else:
        if valor > maior:
            maior = valor
            posmaior = posicao
        if valor < menor:
            menor = valor
            posmenor = posicao

print(f'\nA lista contém os valores: {lista}')

print(f'O MENOR valor é {menor} na posição', end = ' ')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}', end='...')

print(f'\nO MAIOR valor é {maior} na posição', end = ' ')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}', end='...')
