# # for c in range(1,6):
# #     print('Olá, mundo!')


# c = 0
# for c in range(0, 6):
#     print(f'O valor de c é {c}')
#     c = c + 1


# for c in range(0, 7, 2): #O terceiro parâmetro é a quantidade de passos que o laço vai dar, nesse caso, de 2 em 2.
#     print(c)


# n = int(input('Digite um número: '))
# for c in range(0, n+1):
#     print(c)


# inicio = int(input('Digite um número inicial: '))   
# fim = int(input('Digite um número final: '))
# passo = int(input('Digite a quantidade de passos: '))
# for c in range(inicio, fim+1, passo):
#     print(c)


s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n
print(f'\nA soma dos números digitados é {s}')
print('\nFim do programa!')