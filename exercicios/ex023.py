# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
## Ex: Digite um número: 1834
### Unidade: 4
### Dezena: 3
### Centena: 8
### Milhar: 1

num = int(input('Digite um número de 0 a 9999: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10


print('O número digitado foi: {}.'.format(num))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
