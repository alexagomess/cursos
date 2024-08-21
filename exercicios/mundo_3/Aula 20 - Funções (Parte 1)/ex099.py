"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep

def maior(*valores):
    print('-='*30)
    print('\nAnalisando os valores passados...')
    cont = maior = 0
    for vlr in valores:
        print(f'{vlr}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = vlr
        else:
            if vlr > maior:
                maior = vlr
        cont += 1
    print(f'...foram informados {cont} valores ao todo.')
    print(f'O maior número informado foi {maior}.')
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
