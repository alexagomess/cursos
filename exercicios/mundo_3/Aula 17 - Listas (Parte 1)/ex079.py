'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.'''

lista = []

while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado')
    else:
        print('Número já existe na lista.')

    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'\nA lista contém os elementos: {lista}')
lista.sort()
print(f'A lista em ordem crescente é: {lista}')
