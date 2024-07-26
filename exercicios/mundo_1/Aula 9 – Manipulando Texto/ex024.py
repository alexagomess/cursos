# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome = input('Digite o nome de uma cidade: ').strip()

divide = nome.upper().split()

print(divide[0] == 'SANTO')
