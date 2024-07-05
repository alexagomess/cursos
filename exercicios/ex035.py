# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Digite o primeiro valor da reta: '))
r2 = int(input('Digite o segundo valor da reta: '))
r3 = int(input('Digite o terceiro valor da reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas informadas formam um triângulo.')
else:
    print('As retas informadas NÃO formam um triângulo.')
