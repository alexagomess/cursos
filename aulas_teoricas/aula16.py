#Tuplas: As tuplas são imutáveis

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita') 
# print(lanche[2])
# print(lanche[0:2])
# print(lanche[1:])
# print(lanche[-1])

# print(len(lanche))

# for comida in lanche:
#     print(f'Eu vou comer {comida}.')
# print('\nComi muito!!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
    cont += 1
print('\nComi muito!!')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}.')
# print('\nComi muito!!')

# print(sorted(lanche)) #organizar a tupla em ordem alfabética





# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# # print(c)
# # print(sorted(c))
# # print(len(c))
# # print(c.count(2))
# print(c.index(8))