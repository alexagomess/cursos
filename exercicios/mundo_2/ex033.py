# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro e último número: '))

# lista = [n1, n2, n3]
# lista.sort()
# print('O menor número é {}. '.format(lista[0]))
# print('O maior número é {}. '.format(lista[2]))

menor = n1
maior = n1
#veriricando o MENOR numero
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificando o MAIOR numero
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor é {}. '.format(menor))
print('O maior valor é {}. '.format(maior))
