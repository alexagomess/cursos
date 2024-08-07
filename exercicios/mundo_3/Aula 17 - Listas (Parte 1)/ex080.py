'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''


lista = []

for cont in range(0, 5):
    num = int(input('Digite um número: '))
    
    if cont == 0:
        lista.append(num)
    else:
        for posicao, valor in enumerate(lista):
            if num < valor:
                atual = posicao
                break
            if num > valor:
                atual = posicao + 1
        lista.insert(atual, num)
print(f'A lista ordenada é: {lista}')
