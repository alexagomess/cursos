'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='DESCONHECIDO', gols=0):
    if nome == '':
        nome = 'DESCONHECIDO'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

nome_jogador = str(input('Nome do jogador: ')).strip()
qtd_gols = str(input('Número de gols: '))
if qtd_gols.isnumeric():
    qtd_gols = int(qtd_gols)
else:
    qtd_gols = 0

print(ficha(nome_jogador, qtd_gols))