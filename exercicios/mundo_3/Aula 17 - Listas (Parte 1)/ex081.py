'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
cont = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    print('Número adicionado na lista')

    print('\n')
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        print('Programa encerrado')
        break

print(f'\nNúmeros digitados: {cont}')
lista.sort(reverse=True)
print(f'A lista ordenada de forma descrescente: {lista}')

if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
