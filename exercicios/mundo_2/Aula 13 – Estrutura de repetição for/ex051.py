'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''

print('-'*32, '\nCalculo de progressão aritmética\n', '-'*32)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro_termo + (10 - 1) * razao
progressao = 0

print(f'\nO primeiro termo digitado foi {primeiro_termo} e sua progressão aritmética é: ')

for i in range(primeiro_termo, decimo + razao, razao):
    print(f'{i}', end=' ')
