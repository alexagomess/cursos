# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
## 1 para binário
## 2 para octal
## para hexadecimal

numero = int(input('Digite um número inteiro qualquer: '))
base_conversao = int(input('\nAgora escolha a base de conversão. \nEscreva "1" para binário, "2" para octal e "3" para hexadecimal: \n'))

if base_conversao == 1:
    print(f'O número digitado {numero} na base binária é: {bin(numero)[2:]}.')
elif base_conversao == 2:
    print(f'O número digitado {numero} na base octal é: {oct(numero)[2:]}.')
elif base_conversao == 3:
    print(f'O número digitao {numero} na base hexadecimal é {hex(numero)[2:]}.')
else:
    print('Você NÃO digitou uma opção válida! Programa encerrado.')
