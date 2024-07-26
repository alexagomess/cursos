'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

pc = randint(0, 10)

count = 0
user = int(input('Tente adivinhar, qual número o computador pensou? '))
while pc != user:
    print('\nVocê ERROU!!')
    count += 1
    if user > pc:
        user = int(input('DICA: O número é menor do que o que você digitou. Tente adivinhar novamente: '))
    else:
        user = int(input('DICA: O número é maior do que o que você digitou. Tente adivinhar novamente: '))
print(f'\nVocê ACERTOU!! Foram necessárias {count} tentativas até acertar.')
