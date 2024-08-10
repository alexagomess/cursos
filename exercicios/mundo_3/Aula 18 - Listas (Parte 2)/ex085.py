'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = [[], []]

for cont in range(1,8):
    num = int(input(f'Digite o {cont}° número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
    cont += 1
lista[0].sort()
print(f'\nOs valores PARES em ordem crescente são: {lista[0]}')
lista[1].sort()
print(f'Os valores ÍMPARES em ordem crescente são: {lista[1]}\n')
