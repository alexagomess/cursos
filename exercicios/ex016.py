#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
##ex: digite um número: 6.127. O número 6.127 tem a parte inteira 6

from math import trunc

numero = float(input('Digite um número real/float: '))

porcao = trunc(numero)

print('A porção inteira do número {} é de {}.'.format(numero, porcao))
