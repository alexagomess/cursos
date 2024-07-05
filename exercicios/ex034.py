# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
## Para salários superiores a R$1.250,00, calcule um aumento de 10%, para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário para calcularmos seu aumento: R$'))

if salario > 1250:
    percentual = 0.10
    aumento = salario * percentual
    novo_salario = salario + aumento
    print('Baseado no seu salário, seu aumento será de R${:.2f}. Seu novo salário será R${:.2f}.'.format(aumento, novo_salario))
else:
    percentual = 0.15
    aumento = salario * percentual
    novo_salario = salario + aumento
    print('Baseado no seu salário, seu aumento será de R${:.2f}. Seu novo salário será R${:.2f}. '.format(aumento, novo_salario))
