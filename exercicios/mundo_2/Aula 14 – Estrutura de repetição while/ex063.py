'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Exemplo: 0 - 1 - 1 - 2 - 3 - 5 - 8'''

qtd_elementos = int(input('Quantos elementos vc quer ver na sequencia de fibonacci? '))

primeiro_elemento = 0
segundo_elemento = 1
atual = 1
anterior = atual - 1

print(primeiro_elemento, '-', segundo_elemento, '-', end = ' ')
while qtd_elementos != 0:
    atual = atual + anterior
    anterior = atual - anterior

    print(atual, end = ' - ' if qtd_elementos != 1 else '')
    qtd_elementos = qtd_elementos - 1
