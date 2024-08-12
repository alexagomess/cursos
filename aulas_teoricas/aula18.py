# pessoas = [
#     ['pedro', 25],
#     ['maria', 19],
#     ['joao', 32]
# ]
# print(pessoas[0][0]) #vai retornar Pedro
# print(pessoas[1][1])
# print(pessoas[2][0])
# print(pessoas[1])




# teste = list()
# teste.append('Dri')
# teste.append(27)
# print(teste)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Alex'
# teste[1] = 30
# galera.append(teste[:])
# print(galera)





# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for pessoa in galera:
#     # print(pessoa) #printa todas as listas dentro da galera
#     # print(pessoa[0]) #printa apenas os nomes
#     # print(pessoa[1]) #printa apenas as idades
#     print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')





galera = list() #cria uma lista oficial
dados = list() #cria uma lista temporária
menor = maior = 0
for c in range(0, 3):
    dados.append(str(input('Digite um nome: '))) #adiciona o elemento na lista temporaria
    dados.append(int(input('Digite a idade: '))) #adiciona o segundo elemento na lista temporaria
    galera.append(dados[:]) #copia os dados da lista temporária para a lista oficial
    dados.clear() #limpa os dados da lista temporária
print(galera) #printa os dados da lista oficial
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menor += 1
print(f'{maior} são maiores de idade e {menor} são menores de idade.\n')
