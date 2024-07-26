#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

angulo = int(input('Digite um ângulo qualquer: '))
radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print('As medidas do ângulo {} são: '.format(angulo))
print('O seno {:.2f}.'.format(seno))
print('O cosseno {:.2f}.'.format(cosseno))
print('A tangente {:.2f}.'.format(tangente))
