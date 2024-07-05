"""Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes
"""

r1 = int(input('Digite o primeiro valor da reta: '))
r2 = int(input('Digite o segundo valor da reta: '))
r3 = int(input('Digite o terceiro valor da reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas informadas formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('As retas informadas NÃO formam um triângulo.')
