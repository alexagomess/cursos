'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''

somatorio = 0
for i in range(1, 7):
    numero = int(input(f'Digite um número inteiro para a posição {i}: '))
    if numero % 2 == 0:
        somatorio = somatorio + numero
print(f'\nA soma dos números digitados que são pares é {somatorio}.')
