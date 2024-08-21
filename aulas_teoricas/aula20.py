# def mostralinha():
#     print('-'*40)
# mostralinha()
# print('ERRO DO SISTEMA')
# mostralinha()



# def mensagem(texto):
#     print('-'*40)
#     print(texto)
#     print('-'*40)
# mensagem('ERRO DO SISTEMA')



# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma de a + b é {s}\n')
# soma(2, 3)
# soma(5, 9)
# soma(20, 30)



# def contador(*num):
#     for valor in num:
#         print(valor, end=' ')
#     print('FIM')
# contador(2, 1, 7)
# contador(5, 3, 1, 9, 10)
# contador(1)





# def contador(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números.')
# contador(2, 1, 7)
# contador(5, 3, 1, 9, 10)
# contador(1)



# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos += 1
# valores = [7, 2, 5, 10, 0, 2, 9]
# dobra(valores)
# print(valores)




def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
soma(5, 2)
soma(2, 9, 5)