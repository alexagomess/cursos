'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('-'*32, '\nCalculo de progressão aritmética\n', '-'*32)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1

print(f'\nO primeiro termo digitado foi {primeiro_termo} e sua progressão aritmética é: ')

while cont <= 10:
    print(f'{primeiro_termo}', end=' ')
    primeiro_termo += razao
    cont += 1
print('Fim do programa!')
