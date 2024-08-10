'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

temp = []
lista = []

while True:
    nome = str(input('Nome: '))
    temp.append(nome)
    nota_1 = float(input('Nota 1: '))
    temp.append(nota_1)
    nota_2 = float(input('Nota 2: '))
    temp.append(nota_2)

    lista.append(temp[:])
    temp.clear()
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('\nQuer continuar[S/N]? ')).upper()[0]
    if resposta == 'N':
        break
print('-'*40)
print(f'N', end='   ')
print(f'Nome', end='          ')
print(f'Média')
for posicao, valor in enumerate(lista):
    print(f'{posicao}', end='   ')
    print(f'{valor[0]}', end='          ')
    print(f'{(valor[1] + valor[2]) / 2:.1f}')
while True:
    print('-'*40)
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for pos, vlr in enumerate(lista):
        if pos == notas:
            print(f'\nNotas de {vlr[0]} são: {vlr[1]:.1f} e {vlr[2]:.1f}')
    if notas == 999:
        break
