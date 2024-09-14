'''
CONTEÚDO AULA 21 | Funções parte 2
- Interactive Help
- Docstrings
- Argumentos opcionais
- Escopo de variáveis
- Retorno de resultados
'''

# - Docstrings
# def contador(i, f, p):
#     """
#     Faz uma contagem e mostra na tela:
#     - i: inicio da contagem
#     - f: fim da contagem
#     - p: passo da contagem
#     - return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM')
# # contador(0, 100, 10)
# help(contador)



# - Argumentos opcionais
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')
# # somar(3, 2, 5)
# # somar(8, 4)
# somar()


# - Escopo de variáveis  
# def funcao():
#     n1 = 4
#     print(f'N1 dentro vale {n1}.')
# n1 = 2
# funcao()
# print(f'N1 fora vale {n1}.')

# def funcao():
#     global n1
#     n1 = 4
#     print(f'N1 dentro vale {n1}.')
# n1 = 2
# funcao()
# print(f'N1 fora vale {n1}.')



# - Retorno de resultados
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
# r1 = somar(3, 2, 5)
# r2 = somar(8, 4)
# r3 = somar()
# print(f'Os resultados foram {r1}, {r2} e {r3}.')




# PARTE PRÁTICA
# def fatorial(num = 1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
# n = int(input('Digite um número: '))
# print(f'\nO fatorial de {n} é igual a {fatorial(n)}.')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('É ímpar')