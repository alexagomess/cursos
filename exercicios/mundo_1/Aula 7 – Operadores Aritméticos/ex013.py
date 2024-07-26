#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o seu salário: '))

aumento = salario * 0.15
novosalario = salario + aumento

print('O aumento de 15% sobre seu salário foi de R${:.2f}, sendo assim seu novo salário com aumento foi para R${:.2f}'.format(aumento, novosalario))
