#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite um valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print('O valor em metros digitado foi {}. A conversão em centímetros ficou em {} e em milímetros em {}.'.format(metros, centimetros, milimetros))
