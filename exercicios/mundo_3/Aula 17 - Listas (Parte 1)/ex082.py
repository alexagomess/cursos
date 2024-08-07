'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
lista_a = []
lista_b = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    print('Número adicionado na lista')

    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('\nDeseja continuar [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        print('Programa encerrado!')
        break

for valor in lista:
    if valor % 2 == 0:
        lista_a.append(valor)
    else:
        lista_b.append(valor)

print(f'\nA lista tem os elementos: {lista}')
print(f'A lista A tem os elementos PARES: {lista_a}')
print(f'A lista B tem os elementos ÍMPARES: {lista_b}\n')
