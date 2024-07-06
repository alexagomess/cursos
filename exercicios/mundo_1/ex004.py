#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
##e todas as informações possíveis sobre ele
from curses.ascii import isspace, isupper, islower

algo1 = input('Digite algo: ')

print('O tipo primitivo que vc digitou é {}'.format(type(algo1)))
print('Só tem espaço? {}'.format(algo1.isspace()))
print('Está em maiuscula? {}'.format(algo1.isupper()))
print('Está em minuscula? {}'.format(algo1.islower()))
print('Está numerico? {}'.format(algo1.isnumeric()))
print('É alfabetico? {}'.format(algo1.isalpha()))
print('É alfanumerico? {}'.format(algo1.isalnum()))
print('Está captalizado? {}'.format(algo1.istitle()))