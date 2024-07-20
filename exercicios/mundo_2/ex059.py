'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

opcao = 0
while opcao != 5:
    opcao = int(input('''\nDado o menu abaixo:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
\nSelecione sua opção: '''))

    if opcao == 1:
        soma = num1 + num2
        print(f'A soma dos números {num1} e {num2} é a igual {soma}.')
    if opcao == 2:
        mult = num1 * num2
        print(f'A multiplicação dos números {num1} e {num2} é a igual {mult}.')
    if opcao == 3:
        maior = num1
        if num2 > maior:
            maior = num2
            print(f'O maior valor entre {num1} e {num2} é o {maior}.')
        elif maior > num2:
            print(f'O maior valor entre {num1} e {num2} é o {maior}.')
        elif maior == num2:
            print(f'Os dois valores {num1} e {num2} são iguais.')
    if opcao == 4:
        num1 = int(input('Digite o novo primeiro número: '))
        num2 = int(input('Digite o novo segundo número: '))
print('\nFim do programa!')