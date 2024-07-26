'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

numero = int(input('Digite um número inteiro: '))

print('='*10, 'TABUADA DE {}'.format(numero), '='*10)

for i in range(1, 11):
    print('{} * {:2} = {}'.format(numero, i, numero * i))
    
print('='*35)
