'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

pc = randint(1,10)

count = 0
user = int(input('Tente adivinhar, qual número o computador pensou? '))
while pc != user:
    print('\nVocê ERROU!!')
    count += 1
    user = int(input('Tente adivinhar novamente: '))
print(f'\nVocê ACERTOU!! Foram necessárias {count} tentativas até acertar.')
