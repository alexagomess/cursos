'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''

num = int(input('Digite um número para obter o fatorial: '))
atual = num

while num != 0:
    print(num, end = ' x ' if num > 1 else ' = ')
    num -= 1
    if num != 0:
        atual = atual * num
print(atual)
