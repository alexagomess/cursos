'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

dicionario = {}
lista_gols = []
lista_geral = []
cod_incremental = 1

while True:
    soma = 0
    cont = 1
    lista_gols.clear()
    dicionario['Cód'] = cod_incremental
    dicionario['Nome'] = str(input('Nome do jogador: '))
    qtd_partidas = int(input(f'Quantas partidas {dicionario['Nome']} jogou? '))

    while cont <= qtd_partidas:
        gols = int(input(f'Quantos gols na partida {cont}? '))
        lista_gols.append(gols)
        dicionario['Gols'] = lista_gols[:]
        soma += gols
        cont += 1
    dicionario['Total'] = soma
    lista_geral.append(dicionario.copy())
    cod_incremental += 1

    while True:
        resposta = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if resposta in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N.')
        print('-=' * 35)
    if resposta == 'N':
        break

print(lista_geral)
print(f'{'Cód':<4}{'Nome':<12}{'Gols':<6}{'Total':>4}')
for valor in lista_geral:
    print(f'{valor['Cód']:<4}{valor['Nome']:<12}{valor['Gols']}{valor['Total']:>4}')

while True:
    print('-' * 45)
    jogador = int(input('Mostrar dados de qual jogador? '))
    if jogador == 999:
        break
    if jogador > len(lista_geral) or jogador == 0:
        print(f'ERRO! Não existe jogador com código {jogador}.')
    else:
        print('-- LEVANTAMENTO DO JOGADOR', end=' ')
        for dic in lista_geral:
            if dic['Cód'] == jogador:
                print(f'{dic['Nome']}:')
                cont = 1
                for valor in dic['Gols']:
                    print(f'    => Na partida {cont}, fez {valor} gol(s).')
                    cont += 1
                print(f'Foi um total de {dic['Total']} gol(s).\n')
print('\nPrograma encerrado!')
