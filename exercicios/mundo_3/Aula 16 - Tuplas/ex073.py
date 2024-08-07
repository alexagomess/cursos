'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Internacional.'''

times = ('Flamengo','Botafogo','Palmeiras','Fortaleza','Cruzeiro','São Paulo','Bahia','Athletico Paranaense','Atlético-MG',
         'Bragantino','Vasco','Criciúma','Juventude','Internacional','Corinthians','Grêmio','Vitória','Cuiabá','Fluminense','Atlético-GO')

print(f'\nOs 5 primeiros colocados do campeonato brasileiro são: {times[:5]}')
print(f'Os últimos 4 colocados do campeonato brasileiro são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O time Internacional está na posição {times.index('Internacional')+1} da tabela.')
