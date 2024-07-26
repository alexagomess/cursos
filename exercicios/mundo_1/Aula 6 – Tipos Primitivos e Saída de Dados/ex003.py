#Crie um programa que leia dos números e mostre a soma entre eles


num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite um terceiro numero: '))

soma = num1 + num2 - num3

print('A soma entre {} e {} subtraído do {} o total é de {} '.format(num1, num2, num3, soma))