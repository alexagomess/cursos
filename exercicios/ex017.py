#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um trinângulo rentângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt, hypot

oposto = float(input('Digite um valor para o cateto oposto: '))
adjacente = float(input('Digite um valor para o cateto adjacente: '))

# hipotenusa = sqrt(oposto ** 2 + adjacente ** 2)
hipotenusa = hypot(oposto, adjacente)

print('A hipotenusa do triângulo rentângulo é de {:.2f}'.format(hipotenusa))
