# dados = dict()
# dados = {'Nome': 'Pedro', 'Idade': 25}
# print(f'A idade de {dados['Nome']} é {dados['Idade']}.')
# # dados['Sexo'] = 'M' #Para adicionar um novo registro dentro do dict basta faze-lo dessa forma, não tem append
# print(dados)
# del dados['Idade']
# print(dados)




# filme = {
#     'titulo': 'star wars',
#     'ano': 1977,
#     'diretor': 'George Lucas'
# }
# print(filme.values()) #.values conseguimos acessar apenas os valores: ['star wars', 1977, 'George Lucas']
# print(filme.keys()) #.keys conseguimos acessar apenas os títulos: ['titulo', 'ano', 'diretor']
# print(filme.items()) #.items conseguimos acessar todo o dict: [('titulo', 'star wars'), ('ano', 1977), ('diretor', 'George Lucas')]
# for key, value in filme.items():
#     print(f'O {key} é {value}')



# locadora = []
# locadora.append({'titulo': 'star wars','ano': 1977,'diretor': 'George Lucas'})
# locadora.append({'titulo': 'avengers','ano': 2012,'diretor': 'Joss Whedon'})
# locadora.append({'titulo': 'matrix','ano': 1999,'diretor': 'Wachowski'})
# print(locadora)
# print(locadora[0]['ano'])
# print(locadora[2]['titulo'])





# pessoas = {'nome': 'Alex', 'sexo': 'M', 'idade': 30}
# print(pessoas['nome'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

#for key in pessoas.keys():
#     print(key)

# for key, value in pessoas.items():
#     print(f'{key} = {value}')

# del pessoas['sexo']
# for key, value in pessoas.items():
#     print(f'{key} = {value}')

# pessoas['nome'] = 'Gustavo'
# for key, value in pessoas.items():
#     print(f'{key} = {value}')

# pessoas['peso'] = 84
# for key, value in pessoas.items():
#     print(f'{key} = {value}')



# brasil = list()
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# estado3 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
# brasil.append(estado1)
# brasil.append(estado2)
# brasil.append(estado3)
# print(len(brasil))
# print(brasil[0]['uf'])





estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for valor in estado.values():
        print(valor, end=' - ')
    print()