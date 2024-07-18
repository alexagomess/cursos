'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

lista = []
maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da pessoa {i} em kg: '))
    lista.append(peso)

maior_peso = max(lista)
menor_peso = min(lista)    

print(f'\nO maior peso lido foi {maior_peso:.1f}kg.')
print(f'\nO menor peso lido foi {menor_peso:.1f}kg.')
