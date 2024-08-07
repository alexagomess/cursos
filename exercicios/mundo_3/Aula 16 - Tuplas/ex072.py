'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
               'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('\nDigite um número entre 0 e 20 para ve-lo por extenso: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'\nO número digitado {num} é escrito por extenso {num_extenso[num]}.')
