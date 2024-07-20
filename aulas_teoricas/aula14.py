# c = 1
# while c < 10:
#     print('Teste while concluído.')
#     c = c + 1
# print('\nFim do programa!')


# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('\nFim do programa!')


# resposta = 's'
# while resposta == 's':
#     n = int(input('Digite um valor: '))
#     resposta = str(input('\nQuer continuar [S/N]? ')).lower()
#     print('\n')
# print('Fim do programa!')


num = 1
par = impar = 0 
while num != 0:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'\nVocê digitou {par} números pares e {impar} números ímpares.')
print('\nFim do programa!')