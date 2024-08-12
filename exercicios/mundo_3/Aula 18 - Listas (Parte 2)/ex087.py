'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[],[],[],[],[],[],[],[],[]]

for cont in range(9):
    matriz[cont].append(int(input(f'Digite um número: ')))

print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])

soma = 0
for num_par in matriz:
    if num_par[0] % 2 == 0:
        soma += num_par[0]
print(f'\nA soma de todos os valores PARES é: {soma}')

soma_coluna = 0
for pos, valor in enumerate(matriz):
    if pos == 2:
        soma_coluna += valor[0]
    if pos == 5:
        soma_coluna += valor[0]
    if pos == 8:
        soma_coluna += valor[0]
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')

cont = 0
for pos_maior, valor_maior in enumerate(matriz):
    if pos_maior >= 3 and pos_maior <= 8:
        if cont == 0:
            maior = valor_maior
        else:
            if valor_maior > maior:
                maior = valor_maior
        cont += 1
print(f'O maior valor da segunda linha é: {maior[0]}\n')
