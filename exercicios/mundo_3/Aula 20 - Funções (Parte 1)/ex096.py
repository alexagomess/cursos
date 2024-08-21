"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""

def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'\nA área do terreno sendo a largura {largura}m e comprimento {comprimento}m é de {terreno}m2.\n')

# area(comprimento=30, largura=15)

largura_input = float(input('\nLargura (m): '))
comprimento_input = float(input('Comprimento (m): '))
area(largura_input, comprimento_input)
