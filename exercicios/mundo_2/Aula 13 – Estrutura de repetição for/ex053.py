'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: 
- APOS A SOPA
- A SACADA DA CASA
- A TORRE DA DERROTA
- O LOBO AMA O BOLO
- ANOTARAM A DATA DA MARATONA
'''


frase = str(input('Digite uma frase para saber se é um palíndromo ou não: ')).lower().strip()

new_frase = frase[::-1]

print(f'\nA frase digitada foi: {frase}.')
print(f'O inverso da frase é {new_frase}.')
if frase.replace(' ', '') == new_frase.replace(' ', ''):
    print('\nÉ um palíndromo!')
else:
    print('\nNão é um palíndromo!')
