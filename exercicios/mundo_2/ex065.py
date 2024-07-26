'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resposta = 's'
qtd = maior = menor = soma = 0

while resposta in 'Ss':
    num = int(input('\nDigite um número inteiro: '))
    resposta = str(input('\nDeseja continuar? [S/N]: ')).strip().lower()[0]

    qtd = qtd + 1
    soma = soma + num

    if qtd == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / qtd

print(f'\nVocê digitou {qtd} números, a média entre eles é de {media:.1f}, sendo o maior número {maior} e o menor {menor}.')
