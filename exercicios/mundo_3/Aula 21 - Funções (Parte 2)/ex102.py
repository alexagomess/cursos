'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e o outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(valor, show=False):
    """
    Calcula o fatorial de um número.
    - Param valor: O número a ser calculado.
    - Param show: (Opcional) Mostrar ou não a conta do fatorial.
    - Return: O valor do fatorial de um número valor.
    """
    mult = 1
    for c in range(valor, 0, -1):
        if show == True:
            print(c, end=' x ' if c != 1 else ' = ')
        mult *= c
    return f'{mult}'


num = int(input('\nDigite um número para calcular o fatorial: '))
flag = str(input('Deseja mostrar o cálculo [S/N]: ')).upper()[0]
if flag == 'S':
    flag = True
print(fatorial(num, show=flag))
