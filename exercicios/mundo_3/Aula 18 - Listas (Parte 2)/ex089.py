'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

lista = []

while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    lista.append([nome, [nota_1, nota_2], media])

    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('\nQuer continuar[S/N]? ')).upper()[0]
    if resposta == 'N':
        break
print('-'*40)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
for posicao, valor in enumerate(lista):
    print(f'{posicao:<4}{valor[0]:<10}{valor[2]:>8.1f}')
while True:
    print('-'*40)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= len(lista) -1:
        print(f'\nNotas de {lista[opcao][0]} são: {lista[opcao][1][0]:.1f} e {lista[opcao][1][1]:.1f}')
