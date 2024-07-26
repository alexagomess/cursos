# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
## O primeiro valor é maior
## O segundo valor é maior
## Não existe valor maior, os dois são iguais

num_1 = int(input('Digite o primeiro número inteiro: '))
num_2 = int(input('Digite o segundo número inteiro: '))

if num_1 > num_2:
    print(f'\nO PRIMEIRO número {num_1} é maior que o segundo número {num_2}.')
elif num_2 > num_1:
    print(f'\nO SEGUNDO número {num_2} é maior que o primeiro número {num_1}.')
else:
    print(f'\nO dois números são iguais!')
