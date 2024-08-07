'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.'''

# lista_num = tuple(int(input('Digite um número: ')) for c in range(0,4))
lista_num = (int(input('Digite um número: ')),
             int(input('Digite outro número: ')),
             int(input('Digite mais um número: ')),
             int(input('Digite o último número: ')))

print(f'\nVocê digitou os valores: {lista_num}')
print(f'\nO valor 9 apareceu {lista_num.count(9)}')

if 3 in lista_num:
    print(f'O primeiro valor 3 aparece na posição {lista_num.index(3)}')
else:
    print('O valor 3 não foi digitado.')

print(f'Os valores pares são: ', end='')
for cont in range(0, len(lista_num)):
    if lista_num[cont] % 2 == 0:
        print(f'{lista_num[cont]}', end= ' ')
