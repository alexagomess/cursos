nome = str(input('Digite seu nome: ')).strip().lower()

if nome == 'dri':
    print(f'Que nome bonito! ')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é normal.')
print(f'Tenha um bom dia, {nome.title()}!')
