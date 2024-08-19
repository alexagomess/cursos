'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dicionario = {}
lista = []
dicionario['Nome'] = str(input('Nome do jogador: '))
qtd_partidas = int(input(f'Quantas partidas {dicionario['Nome']} jogou? '))
cont = 1
soma = 0

while cont <= qtd_partidas:
    gols = int(input(f'Quantos gols na partida {cont}? '))
    lista.append(gols)
    dicionario['Gols'] = lista[:]
    soma += gols
    cont += 1
dicionario['Total'] = soma
print('-='*35)
print(dicionario)
print('-='*35)
print(f'O jogador {dicionario["Nome"]} jogou {qtd_partidas} partidas, sendo:')
cont = 1
for valor in dicionario["Gols"]:
    print(f'    => Na partida {cont}, fez {valor} gol(s).')
    cont += 1
print(f'Foi um total de {dicionario['Total']} gol(s).')
