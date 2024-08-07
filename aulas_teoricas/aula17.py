#Listas: As listas são mutáveis

# lanche = ['hamburguer', 'suco', 'pizza', 'pudim', 'batata frita']
# print(lanche)
# print(lanche[3])

# lanche.append('cookie')
# print(lanche)

# lanche.insert(0, 'cachorro quente') #insere um item em posição específica da lista
# print(lanche)

# del lanche[3] #remove pela posição
# lanche.pop(3) #remove pela posição
# lanche.remove('suco') #remove pelo valor dentro da lista
# print(lanche)

# lanche.pop() #remove o último elemento da lista

# if 'pizza' in lanche: #verifica se a pizza existe na lista, se sim, remove
#     lanche.remoe('pizza') 






# valores = list(range(4, 11)) #criando uma lista com valores de 4 a 11
# print(valores)

# valores = [8, 2, 5, 4, 9, 3, 0]
# print(valores)
# valores.sort()
# print(valores)
# valores.sort(reverse=True)
# # print(valores)
# # print(f'Essa lista tem {len(valores)} elementos')
# valores.insert(3, 12) #inseriu o 12 na posição 3 da lista
# # print(valores)
# valores.append(99) #inseriu 99 na última posição da lista
# # print(valores)
# valores.pop() #remove o último elemento da lista
# # print(valores)
# valores.pop(3) #removeu o terceiro elemento da lista
# # print(valores)
# valores.remove(0) #removeu o valor zero da lista
# # print(valores)
# if 99 in valores:
#     valores.remove(99)
# else:
#     print('Não tem o valor 99 dentro da lista')
# print(valores)







# lista_valores = [] #ou lista_valores = list() 
# lista_valores.append(5)
# lista_valores.append(9)
# lista_valores.append(4)
# # print(lista_valores)

# # for valores in lista_valores:
# #     print(f'{valores}...', end=' ')

# for posicao, valores in enumerate(lista_valores):
#     print(f'O valor {valores} está na posição {posicao}')







lista = list()
for cont in range(0, 5):
    num = int(input('Digite um número: '))
    lista.append(num)
    print(f'Número digitado: {num}')
    print(f'Posição do número digitado: {cont}')
    print(f'A lista adiconada é: {lista[cont]}')
# print(lista)




# a = [2, 3, 4, 7]
# b = a #aqui o python fez uma ligação entre as listas e não uma cópia
# b[2] = 8 #o valor 8 apareceu em ambas as listas
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')




# a = [2, 3, 4, 7]
# b = a[:] #aqui o python fez uma cópia das listas. Ele copiou todos os elementos da lista A para a lista B
# b[2] = 8 #o valor 8 apareceu apenas na lista B
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')


# lista = [1, 2, 4, 9, 0]
# print(lista[3])
# for c in range(0, 5):
    # print(lista[c])