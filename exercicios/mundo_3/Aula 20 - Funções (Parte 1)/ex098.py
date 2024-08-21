"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada"""

from time import sleep

def contador(inicio, fim, passo):
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim:
        cont = 1
        while cont <= fim:
            print(cont, end= ' ', flush=True)
            cont += passo
            sleep(0.5)
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end= ' ', flush=True)
            cont += passo
            sleep(0.5)
        print('FIM')

contador(1, 10, 1)
contador(10, 0, -2)
print('\nAgora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(inicio=ini, fim=fi, passo=pas)
