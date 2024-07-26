'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''

print('-'*32, '\nCalculo de progressão aritmética\n', '-'*32)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
mais = 10
total = 0

print(f'\nO primeiro termo digitado foi {primeiro_termo} e sua progressão aritmética é: ')

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{primeiro_termo}', end=' ')
        primeiro_termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos temos você quer mostrar a mais? '))
print('Fim do programa!')
